import logging

from reader import read_str
from printer import pr_str
from evaluator import eval_ast
from env import Env

logger = logging.getLogger(__name__)


def READ():
    raw_input = input("user> ")
    if raw_input in ["q", "exit"]:
        raise EOFError
    return read_str(raw_input)


def EVAL(ast, env):
    return eval_ast(ast, env)


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
            status = False
            print("Bye Gitesh :)")
        except Exception as e:
            logger.exception("Exception occurred.\n")


def rep(env):
    command = READ()
    result = EVAL(command, env)
    PRINT(result)
    return


if __name__ == "__main__":
    main()
