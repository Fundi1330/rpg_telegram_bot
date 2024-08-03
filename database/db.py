import sqlite3
from .tables import UserTable, BaseTable

class DataBase():
    def __init__(self, db_path: str) -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.__tables: list[BaseTable] = []
        self.usertable = UserTable(self.cursor, self.connection)

        self.__tables.append(self.usertable)


        self.create_tables()

    def create_tables(self):
        with self.connection:
            for table in self.__tables:
                table.create_table()