from reader import read_str
from printer import pr_str
from evaluator import eval_ast
from mal_types import Number, Symbol, List
from env import Env


def READ():
    raw_input = input("user> ")
    return read_str(raw_input)


def EVAL(ast, env):
    evaluation = eval_ast(ast, env)
    if isinstance(evaluation, List):
        args = [EVAL(elem, env) for elem in evaluation[1:]]
        evaluation = evaluation[0](*args)
    return evaluation


def PRINT(result):
    output = pr_str(result)
    print(output)
    return


def main():
    status = True
    repl_env = Env(outer=None)
    repl_env[Symbol("+")] = lambda a, b: Number(a.value + b.value)
    repl_env[Symbol('-')] = lambda a, b: Number(a.value - b.value)
    repl_env[Symbol('*')] = lambda a, b: Number(a.value * b.value)
    repl_env[Symbol('/')] = lambda a, b: Number(a.value // b.value)
    while status:
        try:
            rep(repl_env)
        except EOFError:
            print("Bye Gitesh :)")
            status = False


def rep(env):
    command = READ()
    result = EVAL(command, env)
    PRINT(result)
    return


if __name__ == "__main__":
    main()
