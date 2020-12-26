from mal_types import Symbol, List


def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        if ast.value not in env:
            raise EnvironmentError(f"Symbol {ast.value} not found in the environment")
        return env[ast.value]
    elif isinstance(ast, List):
        return List([eval_ast(elem, env) for elem in ast])
    else:
        return ast

