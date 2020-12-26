from re import findall
from token_types import Number, Symbol, LeftParen, RightParen


class Reader(object):

    def __init__(self, tokens):
        self.token_list = tokens
        self.current_position = 0

    def _get_current_token(self):
        if (self.current_position >= 0) and (self.current_position < len(self.token_list)):
            return self.token_list[self.current_position]
        else:
            raise OverflowError("Reader: Invalid state encountered.")

    def next(self):
        current_token = self._get_current_token()
        self.current_position += 1
        return current_token

    def peek(self):
        return self._get_current_token()

    def has_reached_EOF(self):
        return self.current_position >= len(self.token_list)


def read_form(parser: Reader):
    current_token = parser.peek()
    if current_token == "(":
        result = read_list(parser)
    else:
        result = read_atom(parser)
    return result


def read_list(parser: Reader):

    if parser.next() != "(":
        raise EnvironmentError("Invalid first token encountered in list.")

    result = [LeftParen()]

    while not parser.has_reached_EOF() and parser.peek() != ")":
        result.append(read_form(parser))

    if parser.has_reached_EOF():
        raise SyntaxError("Missing matching ')' for a list")

    parser.next()
    result.append(RightParen())
    return result


def read_atom(parser: Reader):
    current_token = parser.next()
    if current_token.isdigit():
        result = Number(int(current_token))
    else:
        result = Symbol(current_token)
    return result


def tokenize(input_string: str):
    pattern = r"[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)"
    match = findall(pattern, input_string)
    return [token for token in match if token]


def read_str(raw_input: str):
    tokens = tokenize(raw_input)
    parser = Reader(tokens)
    return read_form(parser)
