import logging
from mal_types import Symbol, Number, List, Boolean, NoneType, FunctionType
from env import Env

logger = logging.getLogger(__name__)


def eval_ast(ast, env):
    return eval_list(ast, env) if isinstance(ast, List) else eval_atom(ast, env)


def eval_atom(atom, env):
    if isinstance(atom, Symbol):
        return env[atom]
    elif isinstance(atom, (Number, Boolean, NoneType)):
        return atom
    else:
        raise NotImplementedError(f"Atom {atom} not yet handled.")


def eval_list(alist, env):
    if isinstance(alist[0], Symbol) and alist[0].is_same_as(Symbol("def!")):
        result = eval_ast(alist[2], env)
        env[alist[1]] = result
    elif isinstance(alist[0], Symbol) and alist[0].is_same_as(Symbol("do")):
        for elem in alist[1:-1]:
            eval_ast(elem, env)
        result = eval_ast(alist[-1], env)
    elif isinstance(alist[0], Symbol) and alist[0].is_same_as(Symbol("if")):
        condition = eval_ast(alist[1], env)
        if isinstance(condition, NoneType) or (isinstance(condition, Boolean) and not condition.value):
            result = eval_ast(alist[3], env) if len(alist) == 4 else NoneType()
        else:
            result = eval_ast(alist[2], env)
    elif isinstance(alist[0], Symbol) and alist[0].is_same_as(Symbol("let*")):
        let_env = Env(outer=env)
        param_bindings = alist[1]
        if not isinstance(param_bindings, List) or len(param_bindings) % 2 != 0:
            raise SyntaxError("Invalid parameter bindings in the `let*` form.")

        i = 0
        while i < len(param_bindings):
            let_env[param_bindings[i]] = eval_ast(param_bindings[i + 1], let_env)
            i += 2

        result = eval_ast(alist[2], let_env)
    elif isinstance(alist[0], Symbol) and alist[0].is_same_as(Symbol("fn*")):
        result = FunctionType(params=alist[1], body=alist[2], env=env)
    else:
        func = eval_ast(alist[0], env)
        args = [eval_ast(elem, env) for elem in alist[1:]]
        if isinstance(func, FunctionType):
            func_env = Env(outer=func.closed_env)
            for k, v in zip(func.parameters, args):
                func_env[k] = v
            result = eval_ast(func.body, env=func_env)
        else:
            result = func(*args)

    return result
