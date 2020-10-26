# exp.py

import math


__all__ = ["calc_exp"]


def calc_exp(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return math.exp(n)


def calc_d_exp(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return math.exp(n)
