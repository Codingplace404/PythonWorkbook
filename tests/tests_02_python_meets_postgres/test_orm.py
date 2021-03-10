import pytest
import psycopg2
import os
from uuid import uuid4
from random import randint
from string import ascii_letters
from pathlib import Path, PurePath
from dotenv import load_dotenv

from tasks._02_python_meets_postgres.orm import (
    Column, Model, PostgresConnector, PostgresManager
)

# from solutions._02_python_meets_postgres.orm import (
#     Column, Model, PostgresConnector, PostgresManager
# )


def get_env_path():
    WORKBOOK_ROOT_DIR = Path(__file__).parent.parent.parent
    ENV_PATH = Path(PurePath(
        WORKBOOK_ROOT_DIR,
        "tasks",
        "_02_python_meets_postgres",
        ".env"
    ))
    return ENV_PATH


def get_postgres_configs():
    db_configs = {
        "host": os.getenv("POSTGRES_HOST"),
        "port": os.getenv("POSTGRES_PORT"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "database": os.getenv("POSTGRES_DATABASE")
    }
    return db_configs


@pytest.fixture
def env_path():
    return get_env_path()


def test_env_file_exists(env_path):
    assert env_path.is_file()


def test_postgres_connection(env_path):
    load_dotenv(dotenv_path=env_path)
    db_configs = get_postgres_configs()
    connector = psycopg2.connect(**db_configs)
    assert connector.status == 1


class TestColumnInit:
    def test_success(self):
        name = "Testcolumn"
        type_ = "int"
        primary_key = True
        column = Column(name=name, type_=type_, primary_key=primary_key)
        assert column.name == name
        assert column.type_ == type_
        assert column.primary_key == primary_key

    def test_raise_key_error_on_not_allowed_type(self):
        name = "Testcolumn"
        type_ = "any_not_suported_field"
        primary_key = True

        with pytest.raises(KeyError):
            Column(name=name, type_=type_, primary_key=primary_key)


class TestColumn:
    def setup_class(self):
        self.name = "Testcolumn"
        self.type_ = "int"

    def test_str_format_for_primary_key_false(self):
        column = Column(name=self.name, type_=self.type_, primary_key=False)
        assert str(column) == f"{self.name} {self.type_}"

    def test_str_format_for_primary_key_true(self):
        column = Column(name=self.name, type_=self.type_, primary_key=True)
        assert "primary key" in str(column).lower()


class TestModelInit:
    def test_success(self):
        columns = [
            Column(name="index", type_="serial", primary_key=True),
            Column(name="random_string", type_="varchar"),
            Column(name="random_int", type_="int"),
        ]
        table_name = "TestTable"
        model = Model(table_name=table_name, columns=columns)
        assert model.table_name == table_name
        assert model.columns == columns

    def test_raise_value_error_on_multiple_primary_keys(self):
        columns = [
            Column(name="index", type_="serial", primary_key=True),
            Column(name="random_string", type_="varchar"),
            Column(name="random_int", type_="int"),
            Column(name="error_index", type_="serial", primary_key=True)
        ]
        table_name = "TestTable"
        with pytest.raises(ValueError):
            Model(table_name=table_name, columns=columns)


def test_postgres_connector_init(env_path):
    load_dotenv(dotenv_path=env_path)
    db_configs = get_postgres_configs()
    connector = PostgresConnector(**db_configs)
    assert connector.connector.status == 1
    assert connector.cursor is not None
    assert isinstance(connector.cursor, psycopg2.extensions.cursor)


class PostgresIntegrationTestBase:
    def setup_class(self):
        load_dotenv(dotenv_path=get_env_path())
        db_configs = get_postgres_configs()
        self.connector = PostgresConnector(**db_configs)

        self.columns = [
            Column(name="index", type_="int", primary_key=True),
            Column(name="random_string", type_="varchar"),
            Column(name="random_int", type_="int"),
        ]

        self.table_name = "".join([
            ascii_letters[randint(0, len(ascii_letters)-1)] for _ in range(20)
        ])
        self.model = Model(
            table_name=self.table_name,
            columns=self.columns
        )

    def setup_method(self):
        columns = ",".join([str(column) for column in self.columns])
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({columns})"
        self.connector.cursor.execute(sql)

    def teardown_class(self):
        self.connector.cursor.close()
        self.connector.connector.close()

    def teardown_method(self):
        sql = f"DROP TABLE IF EXISTS {self.table_name}"
        self.connector.cursor.execute(sql)


class TestPostgresConnector(PostgresIntegrationTestBase):
    def test_create_table(self):
        table_name = "".join([
            ascii_letters[randint(0, len(ascii_letters)-1)] for _ in range(20)
        ])
        self.connector.create_table(
            table_name=table_name,
            columns=self.columns
        )

        # If drop is successfull: table was successfully created before
        drop_table_sql = f"DROP TABLE {table_name};"
        self.connector.cursor.execute(drop_table_sql)
        assert True

    def test_drop_table(self):
        table_name = "".join([
            ascii_letters[randint(0, len(ascii_letters)-1)] for _ in range(20)
        ])
        columns = ",".join([str(column) for column in self.columns])
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.connector.cursor.execute(sql)

        self.connector.drop_table(table_name=table_name)
        table_exists_sql = """
            SELECT EXISTS (
                SELECT * FROM information_schema.tables
                WHERE table_name=%s
            )
        """
        self.connector.cursor.execute(table_exists_sql, [table_name])
        table_exists = self.connector.cursor.fetchone()[0]
        assert not table_exists

    def test_insert_single_row(self):
        row = [1, uuid4().hex[:8], randint(1000, 9999)]
        get_sql = f"SELECT * FROM {self.table_name} WHERE index=1"
        self.connector.cursor.execute(get_sql)
        assert len(self.connector.cursor.fetchall()) == 0

        self.connector.single_row_insert(
            table_name=self.table_name,
            columns=self.columns,
            row=row
        )

        self.connector.cursor.execute(get_sql)
        assert len(self.connector.cursor.fetchall()) == 1

    def test_bulk_row_insert(self):
        get_sql = f"SELECT * FROM {self.table_name} WHERE index < 101"
        self.connector.cursor.execute(get_sql)
        assert len(self.connector.cursor.fetchall()) == 0
        rows = [
            [index, uuid4().hex[:8], randint(1000, 9999)]
            for index in range(1, 101)
        ]

        self.connector.bulk_row_insert(
            table_name=self.table_name,
            columns=self.columns,
            rows=rows
        )
        self.connector.cursor.execute(get_sql)
        assert len(self.connector.cursor.fetchall()) == 100


def test_postgres_manager_init(env_path):
    load_dotenv(dotenv_path=env_path)
    db_configs = get_postgres_configs()
    connector = PostgresConnector(**db_configs)
    columns = [
        Column(name="index", type_="int", primary_key=True),
        Column(name="random_string", type_="varchar"),
        Column(name="random_int", type_="int"),
    ]
    table_name = "TestTable"
    model = Model(table_name=table_name, columns=columns)
    postgres_manager = PostgresManager(connector=connector, model=model)
    assert postgres_manager.connector == connector
    assert postgres_manager.model == model


class TestPostgresManager(PostgresIntegrationTestBase):
    def setup_class(self):
        super().setup_class(self)
        self.postgres_manager = PostgresManager(
            connector=self.connector,
            model=self.model
        )

    def test_migrate(self):
        table_name = "".join([
            ascii_letters[randint(0, len(ascii_letters)-1)] for _ in range(20)
        ])
        model = Model(table_name=table_name, columns=self.columns)
        postgres_manager = PostgresManager(
            connector=self.connector,
            model=model
        )

        postgres_manager.migrate()

        # If drop is successfull: table was successfully created before
        drop_table_sql = f"DROP TABLE {table_name};"
        self.connector.cursor.execute(drop_table_sql)
        assert True

    def test_insert_single_row(self):
        row = [1, uuid4().hex[:8], randint(1000, 9999)]
        get_sql = f"SELECT * FROM {self.table_name} WHERE index=1"
        self.connector.cursor.execute(get_sql)
        assert len(self.connector.cursor.fetchall()) == 0

        self.postgres_manager.insert(row=row)

        self.connector.cursor.execute(get_sql)
        assert len(self.connector.cursor.fetchall()) == 1

    def test_bulk_row_insert(self):
        get_sql = f"SELECT * FROM {self.table_name} WHERE index < 101"
        self.connector.cursor.execute(get_sql)
        assert len(self.connector.cursor.fetchall()) == 0
        rows = [
            [index, uuid4().hex[:8], randint(1000, 9999)]
            for index in range(1, 101)
        ]

        self.postgres_manager.bulk_insert(rows=rows)

        self.connector.cursor.execute(get_sql)
        assert len(self.connector.cursor.fetchall()) == 100
