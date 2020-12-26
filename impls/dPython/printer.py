from token_types import Number, Symbol, LeftParen, RightParen


def pr_str(result, sep=" "):

    if isinstance(result, list):
        output = ""
        for i, elem in enumerate(result):
            sep = "" if i < len(result) - 1 and isinstance(result[i+1], RightParen) else " "
            output += pr_str(elem, sep=sep)
    elif isinstance(result, Number):
        output = str(result.value) + sep
    elif isinstance(result, (LeftParen, RightParen)):
        output = result.value
    elif isinstance(result, Symbol):
        output = result.value + sep
    else:
        raise NotImplementedError("Invalid token: Token not yet implemented.")

    return output
