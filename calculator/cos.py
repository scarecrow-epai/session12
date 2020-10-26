# cos.py

import math


__all__ = ["calc_cos", "constant"]

constant = 3.14


def calc_cos(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return math.cos(n)


def calc_d_cos(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return -1 * math.sin(n)
