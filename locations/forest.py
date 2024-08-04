from .base import BaseLocation
from enemies import Troll

class Forest(BaseLocation):
    name = 'Forest'
    enemies = [Troll]