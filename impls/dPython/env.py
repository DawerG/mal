import logging
from mal_types import Number, Symbol

logger = logging.getLogger(__name__)


class Env(object):
    def __init__(self, outer):
        self.map = {}
        if outer is None:
            self.initialize()
        self.parent = outer

    def find(self, symbol):
        key = symbol.value
        if key in self.map:
            return self
        elif self.parent is not None:
            return self.parent.find(symbol)
        else:
            raise ValueError(f"Symbol {key} not found in the environment.")

    def __setitem__(self, symbol, value):
        key = symbol.value

        if key in self.map:
            logger.warning(f" Symbol {key} already exists in the environment.")

        self.map[key] = value

    def __getitem__(self, symbol):
        key = symbol.value
        return self.find(symbol).map[key]

    def initialize(self):
        self[Symbol("+")] = lambda a, b: Number(a.value + b.value)
        self[Symbol('-')] = lambda a, b: Number(a.value - b.value)
        self[Symbol('*')] = lambda a, b: Number(a.value * b.value)
        self[Symbol('/')] = lambda a, b: Number(a.value // b.value)
