from re import search

def isInteger(string: str):
    result = False
    if search(r"-*[0-9]+", string):
        result = True
    return result