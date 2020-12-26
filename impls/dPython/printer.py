from mal_types import Number, Symbol, List


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
    else:
        raise NotImplementedError("Invalid token: Token not yet implemented.")

    return output
