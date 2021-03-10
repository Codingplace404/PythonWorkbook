import psycopg2
from psycopg2.extras import execute_values
from typing import List


class Column:
    allowed_types = ["int", "serial", "decimal", "varchar", ]

    def __init__(self, name: str, type_: str, primary_key: bool = False):
        """Constructs all the necessary attributes for the Column object.

        :param name: name of Column
        :param type_: Type of column. Type should be in `allowed_types`
        :param primary_key: info if column is primary key

        :raises: `KeyError` if `type_` is not in `allowed_types`
        """
        self.name = name
        if type_ not in self.allowed_types:
            raise KeyError(
                f"`type_` must be in {self.allowed_types} but it's {type_}"
            )
        self.type_ = type_
        self.primary_key = primary_key

    def __str__(self) -> str:
        """Returns __str__ of object.

        :returns: combination of name and type_.
            Formatted as "NAME TYPE_ [PRIMARY KEY]"
        """
        if self.primary_key:
            return f"{self.name} {self.type_} PRIMARY KEY"
        return f"{self.name} {self.type_}"


class Model:
    def __init__(self, table_name: str, columns: List[Column]):
        """Constructs all necessary attributes for the Model object.
            Just one Primary Key is supported.

        :params table_name: Name of Table
        :params columns: Columns of Table
        :rasises: Value Error if more than one Primary Key is in columns
        """
        self.table_name = table_name

        primary_key = None
        for column in columns:
            if column.primary_key:
                if primary_key is not None:
                    raise ValueError(
                        "Model can have at maximum 1 primary key."
                    )
                primary_key = column

        self.columns = columns


class PostgresConnector:
    """!!! SQL Injection is not well protected !!!"""

    def __init__(self, **configs):
        """Constructs connector and cursor for the PostgresConnector object.

        :param configs: Configs for postgres, e.g.
            host, port, user, password, database
        """
        self.connector = psycopg2.connect(**configs)
        self.connector.set_session(autocommit=True)
        self.cursor = self.connector.cursor()

    def create_table(self, table_name: str, columns: List[Column]):
        """Creates a database table

        :param table_name: name of table which should be created
        :param columns: List of columns which should be created
        """
        columns = ",".join([str(column) for column in columns])
        sql = f"CREATE TABLE {table_name} ({columns})"
        self.cursor.execute(sql)

    def drop_table(self, table_name: str):
        """Drops a database table

        :param table_name: name of table which should be deleted
        """
        sql = f"DROP TABLE {table_name}"
        self.cursor.execute(sql)

    def single_row_insert(self, table_name: str, columns: List[Column],
                          row: List):
        """Inserts a single row into postgres table

        :param table_name: name of table where row should be inserted in
        :param columns: list of columns of table values
        :param row: list of values which should be inserteted
        """
        columns = ", ".join([column.name for column in columns])
        values = ", ".join(["%s" for _ in row])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(sql, row)

    def bulk_row_insert(self, table_name: str, columns: List[Column],
                        rows: List[List]):
        """Inserts a multiple rows into postgres table

        :param table_name: name of table where row should be inserted in
        :param columns: list of columns of table values
        :param rows: list of rows which should be inserteted
        """
        columns = ", ".join([column.name for column in columns])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES %s"
        execute_values(cur=self.cursor, sql=sql, argslist=rows)


class PostgresManager:
    def __init__(self, connector: PostgresConnector, model: Model):
        """Constructs connector Manager object and other necessary attributes
            for the PostgresManager object. Just one Primary Key is supported.

        :params connector: Postgres Connector
        :params model: Model which should be managed
        """
        self.connector = connector
        self.model = model

    def migrate(self):
        """Migrates Model into database. Currently only create
            is supported.
        """
        self.connector.create_table(
            table_name=self.model.table_name,
            columns=self.model.columns
        )

    def insert(self, row: List):
        """Inserts a single row into table

        :param row: List of values to insert.
        """
        self.connector.single_row_insert(
            table_name=self.model.table_name,
            columns=self.model.columns,
            row=row
        )

    def bulk_insert(self, rows: List[List]):
        """Inserts a bulk of rows into table

        :param row: List of rows to insert.
        """
        self.connector.bulk_row_insert(
            table_name=self.model.table_name,
            columns=self.model.columns,
            rows=rows
        )
