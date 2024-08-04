from abc import ABCMeta, abstractmethod  
from enemies import BaseEnemy
from typing import Any
from random import choices

class BaseLocation(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name() -> str:
        '''The name of the location'''

    @property
    @abstractmethod
    def enemies() -> list[BaseEnemy[Any]]:
        '''The list of enemies which can be found on a location'''

    def get_enemy(self) -> BaseEnemy[Any]:
        '''Gets a weight random enemy'''
        weights = [e.weight for e in self.enemies]

        return choices(self.enemies, weights)[0]


    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name