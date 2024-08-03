from json import loads
from os import environ
from database import DataBase

config_path = environ.get('CONFIG_PATH')

current_config: dict = {}



with open(config_path, 'r', encoding='utf-8') as config:
    current_config = loads(config.read())

db: DataBase = DataBase(current_config.get('database_path'))