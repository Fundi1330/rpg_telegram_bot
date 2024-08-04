from abc import ABCMeta, abstractmethod
from random import randint


class BaseEnemy(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.health = randint(self.min_health, self.max_health)
        self.defence = randint(self.min_defence, self.max_defence)
        self.attack = randint(self.min_attack, self.max_attack)\
        
    
    @property
    @abstractmethod
    def min_health() -> int:
        '''Minimum health of an enemy'''
    
    @property
    @abstractmethod
    def max_health() -> int:
        '''Maximum health of an enemy'''

    @property
    @abstractmethod
    def min_defence() -> int:
        '''Minimum defence of an enemy'''
    
    @property
    @abstractmethod
    def max_defence() -> int:
        '''Maximum defence of an enemy'''

    @property
    @abstractmethod
    def min_attack() -> int:
        '''Minimum attack of an enemy'''
    
    @property
    @abstractmethod
    def max_attack() -> int:
        '''Maximum attack of an enemy'''

    @property
    @abstractmethod
    @staticmethod
    def weight() -> float:
        '''Chance of getting enemy in location'''