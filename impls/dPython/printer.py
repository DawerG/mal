from mal_types import Number, Symbol, List, Boolean, NoneType


def pr_str(result):
    if isinstance(result, List):
        output = "("
        for i, elem in enumerate(result):
            sep = "" if i == len(result) - 1 else " "
            output += pr_str(elem) + sep
        output += ")"
    elif isinstance(result, Number):
        output = str(result.value)
    elif isinstance(result, Symbol):
        output = result.value
    elif isinstance(result, Boolean):
        output = "true" if result.value else "false"
    elif isinstance(result, NoneType):
        output = "nil"
    else:
        raise NotImplementedError("Invalid token: Token not yet implemented.")

    return output
