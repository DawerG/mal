class MalType(object):
    pass


class List(MalType):

    def __init__(self, init_list):
        self.list = init_list

    def append(self, elem: MalType):
        self.list.append(elem)

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return len(self.list)

    def __eq__(self, other):
        if isinstance(other, List):
            return len(other) == len(self) and all((i == j).value for i, j in zip(other.list, self.list))
        return Boolean(False)


class Number(MalType):

    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Number):
            return Boolean(other.value == self.value)
        return Boolean(False)


class Symbol(MalType):

    def __init__(self, value: str):
        self.value = value

    def is_same_as(self, symbol):
        return self.value == symbol.value

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return Boolean(other.value == self.value)
        return Boolean(False)


class Boolean(MalType):

    def __init__(self, value: bool):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Boolean):
            return Boolean(other.value == self.value)
        return Boolean(False)


class NoneType(MalType):

    def __init__(self):
        self.value = None

    def __eq__(self, other):
        return isinstance(other, NoneType)


class FunctionType(MalType):

    def __init__(self, params, body, env):
        self.parameters = params
        self.body = body
        self.closed_env = env

