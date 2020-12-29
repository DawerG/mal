from re import search


def is_integer(string: str):
    result = False
    if search(r"^\-?[0-9]+$", string):
        result = True
    return result
