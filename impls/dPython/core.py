from mal_types import Symbol, Number, List, NoneType, Boolean
from printer import pr_str


def core_prn(arg):
    print(pr_str(arg, print_readably=True))
    return NoneType()


def core_list(*args):
    return List(args)


def core_is_list(arg):
    return Boolean(isinstance(arg, List))


def core_is_list_empty(arg: List):
    return Boolean(len(arg.list) == 0)


def core_list_count(arg: List):
    return Number(len(arg.list))


def core_equal(first, second):
    return first == second


namespace = (
    (Symbol("+"), lambda a, b: Number(a.value + b.value)),
    (Symbol("-"), lambda a, b: Number(a.value - b.value)),
    (Symbol("*"), lambda a, b: Number(a.value * b.value)),
    (Symbol("/"), lambda a, b: Number(a.value // b.value)),

    (Symbol("<"), lambda a, b: Boolean(a.value < b.value)),
    (Symbol("<="), lambda a, b: Boolean(a.value <= b.value)),
    (Symbol(">"), lambda a, b: Boolean(a.value > b.value)),
    (Symbol(">="), lambda a, b: Boolean(a.value >= b.value)),

    (Symbol("="), core_equal),
    (Symbol("prn"), core_prn),
    (Symbol("list"), core_list),
    (Symbol("list?"), core_is_list),
    (Symbol("empty?"), core_is_list_empty),
    (Symbol("count"), core_list_count),
)


