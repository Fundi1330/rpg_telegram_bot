import sqlite3
from .tables import UserTable, BaseTable, StatsTable
from typing import Any

class DataBase():
    def __init__(self, db_path: str) -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.__tables: list[BaseTable[Any]] = []
        self.usertable = UserTable(self.cursor, self.connection)
        self.statstable = StatsTable(self.cursor, self.connection)
        self.__tables.append(self.usertable)
        self.__tables.append(self.statstable)


        self.create_tables()

    def create_tables(self):
        with self.connection:
            for table in self.__tables:
                table.create_table()