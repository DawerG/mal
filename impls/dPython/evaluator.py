from mal_types import Symbol, List


def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        return env[ast]
    elif isinstance(ast, List):
        return List([eval_ast(elem, env) for elem in ast])
    else:
        return ast

