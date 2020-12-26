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


class Number(MalType):

    def __init__(self, value: int):
        self.value = value


class Symbol(MalType):

    def __init__(self, value: str):
        self.value = value

    def is_same_as(self, symbol):
        return self.value == symbol.value
