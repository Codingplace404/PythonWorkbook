# import psycopg2
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
        pass

    def __str__(self) -> str:
        """Returns __str__ of object.

        :returns: combination of name and type_.
            Formatted as "NAME TYPE_ [PRIMARY KEY]"
        """
        pass


class Model:
    """Database Model. This class inherits from PostgresManager class."""

    def __init__(self, table_name: str, columns: List[Column]):
        """Constructs all the necessary attributes for the Model object.
        Just one Primary Key is supported.

        :params table_name: Name of Table
        :params columns: Columns of Table
        :rasises: Value Error if more than one Primary Key is in columns
        """
        pass


class PostgresConnector:
    """!!! SQL Injection is not well protected !!!
    """
    def __init__(self, **configs):
        """Constructs connector and cursor for the PostgresConnector object.

        :param configs: Configs for postgres, e.g.
            host, port, user, password, database
        """
        pass

    def create_table(self, table_name: str, columns: List[Column]):
        """Creates a database table

        :param table_name: name of table which should be created
        :param columns: List of columns which should be created
        """
        pass

    def drop_table(self, table_name: str):
        """Drops a database table

        :param table_name: name of table which should be deleted
        """
        pass

    def single_row_insert(self, table_name: str, columns: List[Column],
                          row: List):
        """Inserts a single row into postgres table

        :param table_name: name of table where row should be inserted in
        :param columns: list of columns of table values
        :param row: list of values which should be inserteted
        """
        pass

    def bulk_row_insert(self, table_name: str, columns: List[Column],
                        rows: List[List]):
        """Inserts a multiple rows into postgres table

        :param table_name: name of table where row should be inserted in
        :param columns: list of columns of table values
        :param rows: list of rows which should be inserteted
        """
        pass


class PostgresManager:
    connector = PostgresConnector

    def __init__(self, connector: PostgresConnector, model: Model):
        """Constructs connector Manager object and other necessary attributes
            for the PostgresManager object. Just one Primary Key is supported.

        :params connector: Postgres Connector
        :params model: Model which should be managed
        """
        pass

    def migrate(self):
        """Migrates Model into database. Currently only create
            is supported.
        """
        pass

    def insert(self, row: List):
        """Inserts a single row into table

        :param row: List of values to insert.
        """
        pass

    def bulk_insert(self, rows: List[List]):
        """Inserts a bulk of rows into table

        :param row: List of rows to insert.
        """
        pass
