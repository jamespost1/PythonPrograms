# CSCI 220/620
# Summer 2022
# Assignment 1 - Propositional Logic
# James Post


import inspect
import pandas as pd
from itertools import product


def get_func_body(f):
    body = inspect.getsource(f)
    idx = body.index("return")
    return '"' + body[7 + idx:].strip() + '"'


def f_not(x):
    return ~x


def f_and(x, y):
    return x and y


def f_or(x, y):
    return x or y


def f_xor(x, y):
    return x ^ y


def f_impl(x, y):
    return not x or y


def f_bi_impl(x, y):
    return f_impl(x, y) and f_impl(y, x)


def f_rev_impl(x, y):
    return f_impl(y, x)


def f0(p, q, r):
    return (p or q) and r


def f1(p):
    return p and not p


def f2(p):
    return p or not p


def f3(p, q):
    return not p and f_impl(p, q)


def f4(p, q):
    return f_impl(p, q) or f_rev_impl(p, q)


def f5(p, q):
    return (p or q) or (not p and not q)


def f6(p, q):
    return (p or q) and (not p and not q)


def f7(p, q, r):
    return f_impl(p, q) and f_impl(q, r)


# Hypothetical Syllogism
def f8(p, q, r):
    return f_impl(f_impl(p, q) and f_impl(q, r), f_impl(p, r))


# DeMorgan's First Law
def f9(p, q):
    return f_bi_impl(not (p or q), (not p and not q))


# DeMorgan's Second Law
def f10(p, q):
    return f_bi_impl(not (p and q), (not p or not q))


def f11(p, q):
    return f_bi_impl(not(p or (not p and q)), (not p and not q))


def f12(p, q, r):
    return f_bi_impl(not (f_impl(p, q)) or f_impl(r, p), (p or not r or p) and (not q or not r or p))


# https://stackoverflow.com/questions/29548744/creating-a-truth-table-for-any-expression-in-python
def truth_table(f):
    values = [list(x) + [f(*x)] for x in product([False, True], repeat=f.__code__.co_argcount)]
    return pd.DataFrame(values, columns=(list(f.__code__.co_varnames) + [f.__name__]))


def analyze_truth_table(f):
    tt = truth_table(f)
    tt_rows = tt.shape[0]
    tt_cols = tt.shape[1]
    tt_vars = tt_cols - 1
    last_col = tt.iloc[:, tt_vars]
    if last_col.all():
        tt_type = "Tautology"
    elif last_col.any():
        tt_type = "Contingency"
    else:
        tt_type = "Contradiction"
    print("Name:", f.__name__, get_func_body(f))
    print(tt)
    print("Rows:", tt_rows, ", Cols:", tt_cols, ", Vars:", tt_vars, ", Type:", tt_type)
    print()


def main():
    functions = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]
    for function in functions:
        analyze_truth_table(function)


if __name__ == "__main__":
    main()
