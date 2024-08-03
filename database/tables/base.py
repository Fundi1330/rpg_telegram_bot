from sqlite3 import Cursor, Connection
from abc import ABCMeta, abstractmethod
from typing import Any

class BaseTable(metaclass=ABCMeta):
    def __init__(self, cursor: Cursor, connection: Connection) -> None:
        self.cursor = cursor
        self.connection = connection

    @abstractmethod
    def create_table(self) -> None:
        '''Creates a table'''

    @abstractmethod
    def get_all(self) -> list[tuple]:
        '''Get all rows from  atable'''

    @abstractmethod
    def get_first(self, telegram_id: Any) -> tuple:
        '''Get first row from a table'''

    @abstractmethod
    def insert(self, values: list) -> None:
        '''Insert row into a table''' 
    
    @abstractmethod
    def update(self, telegram_id: int, **kwargs) -> None:
        '''Update row(s) in table''' 

    @abstractmethod
    def delete(self, telegram_id: int) -> None:
        '''Delete tow from a table'''

    def row_exists(self, id):
        '''Returns true if row exists, otherwise false'''
        if self.get_first(id):
            return True
        
        return False
        