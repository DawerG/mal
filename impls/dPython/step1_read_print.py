from reader import read_str
from printer import pr_str


def READ():
    raw_input = input("user> ")
    return read_str(raw_input)


def EVAL(command: str):
    return command


def PRINT(result):
    output = pr_str(result)
    print(output)
    return


def main():
    status = True
    while status:
        try:
            rep()
        except EOFError:
            print("Bye Gitesh :)")
            status = False


def rep():
    command = READ()
    result = EVAL(command)
    PRINT(result)
    return


if __name__ == "__main__":
    main()
