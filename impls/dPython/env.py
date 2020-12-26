import logging
class Env(object):
    def __init__(self, outer):
        self.map = {}
        self.parent = outer

    def __setitem__(self, symbol, value):
        key = symbol.value

        if key in self.map:
            logging.warning(f" Symbol {key} already exists in the environment.")

        self.map[key] = value

    def find(self, symbol):
        key = symbol.value
        if key in self.map:
            return self
        elif self.parent is not None:
            return self.parent.find(symbol)
        else:
            raise ValueError(f"Symbol {key} not found in the environment.")

    def __getitem__(self, symbol):
        key = symbol.value
        return self.find(symbol).map[key]