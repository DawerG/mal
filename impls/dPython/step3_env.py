from reader import read_str
from printer import pr_str
from evaluator import eval_ast
from mal_types import Number, Symbol, List
from env import Env


def READ():
    raw_input = input("user> ")
    return read_str(raw_input)


def EVAL(ast, env):
    if isinstance(ast,  List):
        if isinstance(ast[0], Symbol) and ast[0].is_same_as(Symbol("def!")):
            result = EVAL(ast[2], env)
            env[ast[1]] = result
        elif isinstance(ast[0], Symbol) and ast[0].is_same_as(Symbol("let*")):
            let_env = Env(outer=env)
            param_bindings = ast[1]
            if not isinstance(param_bindings, List) or len(param_bindings) % 2 != 0:
                raise SyntaxError("Invalid parameter bindings in the `let*` form.")

            i = 0
            while i < len(param_bindings):
                let_env[param_bindings[i]] = EVAL(param_bindings[i+1], let_env)
                i += 2

            result = EVAL(ast[2], let_env)
        else:
            func = EVAL(ast[0], env)
            args = [EVAL(elem, env) for elem in ast[1:]]
            result = func(*args)
    else:
        result = eval_ast(ast, env)

    return result


def PRINT(result):
    output = pr_str(result)
    print(output)
    return


def main():
    status = True
    repl_env = Env(outer=None)
    while status:
        try:
            rep(repl_env)
        except EOFError:
            print("Bye Gitesh :)")
            status = False
        except Exception as e:
            print(e)

def rep(env):
    command = READ()
    result = EVAL(command, env)
    PRINT(result)
    return


if __name__ == "__main__":
    main()
