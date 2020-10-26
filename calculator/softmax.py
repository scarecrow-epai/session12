# softmax.py

import math


__all__ = ["calc_softmax"]


def calc_softmax(n):
    if not isinstance(n, list) and not isinstance(n, tuple):
        raise ValueError("n should be a list/tuples of numbers.")

    exp_list = [math.exp(i) for i in n]
    sum_exp = sum(exp_list)
    final_vals = [i / sum_exp for i in exp_list]

    return final_vals


def calc_d_softmax(n):
    if not isinstance(n, list) and not isinstance(n, tuple):
        raise ValueError("n should be a number.")

    s = calc_softmax(n)
    so = [1 - i for i in s]

    return [a * b for a, b in zip(s, so)]
