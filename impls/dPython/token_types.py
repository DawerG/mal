class Token(object):
    pass


class LeftParen(Token):

    def __init__(self):
        self.value = "("


class RightParen(Token):

    def __init__(self):
        self.value = ")"


class Number(Token):

    def __init__(self, value):
        self.value = value


class Symbol(Token):

    def __init__(self, value: str):
        self.value = value