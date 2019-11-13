import enum
from typing import Iterable


class Cheeses(enum.Enum):
    """Enumeration of cheeses that we know about"""

    BRIE = 'brie'
    CAMEMBERT = 'camembert'
    CHEDDAR = 'cheddar'
    EDAM = 'edam'
    STILTON = 'stilton'


class CheeseBoard(object):
    """A collection of delicious cheeses that can be enjoyed after dinner"""

    def __init__(self, cheeses: Iterable[Cheeses]):
        """

        :param cheeses: Cheese to put on the board
        """
        self._contents = list(cheeses)

    @property
    def portion_count(self):
        """The number of cheese portions on the boards"""
        return len(self._contents)

    def take_cheese(self):
        """Takes the last portion of cheese added to the board, removing it from the board"""
        return self._contents.pop()

    def has_cheese(self, cheese):
        """Checks whether a given cheese is on the board"""
        return cheese in self._contents
