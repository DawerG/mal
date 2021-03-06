from re import findall
from mal_types import Number, Symbol, List, Boolean, NoneType
from helper_utils import is_integer

matching_token = {
    "[": "]",
    "(": ")"
}


class Reader(object):

    def __init__(self, tokens):
        self.token_list = tokens
        self.current_position = 0

    def _get_current_token(self):
        if (self.current_position >= 0) and (self.current_position < len(self.token_list)):
            return self.token_list[self.current_position]
        else:
            raise IndexError("Reader: Invalid state encountered.")

    def next(self):
        current_token = self._get_current_token()
        self.current_position += 1
        return current_token

    def peek(self):
        return self._get_current_token()

    def has_reached_EOF(self):
        return self.current_position >= len(self.token_list)


def read_form(parser: Reader):
    return read_list(parser) if parser.peek() in matching_token else read_atom(parser)


def read_list(parser: Reader):

    begin_token = parser.next()
    if begin_token not in matching_token:
        raise SyntaxError("Invalid first token encountered in list.")

    result = List([])

    while not parser.has_reached_EOF() and parser.peek() != matching_token[begin_token]:
        result.append(read_form(parser))

    if parser.has_reached_EOF():
        raise SyntaxError("Missing matching ')' for a list")

    parser.next()
    return result


def read_atom(parser: Reader):
    current_token = parser.next()
    if is_integer(current_token):
        result = Number(int(current_token))
    elif current_token in ["true", "false"]:
        result = Boolean(True if current_token == "true" else False)
    elif current_token == "nil":
        result = NoneType()
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
