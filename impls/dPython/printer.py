from mal_types import Number, Symbol, List, Boolean, NoneType, FunctionType


def pr_str(result, print_readably=True):
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
    elif isinstance(result, FunctionType):
        output = "#<function>"
    else:
        raise NotImplementedError("Invalid Type: Type {result} not yet implemented.")

    return output
