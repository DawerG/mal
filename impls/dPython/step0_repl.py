def READ():
    tokens = input("user> ")
    return tokens


def EVAL(command: str):
    return command


def PRINT(result: str):
    print(result)
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
