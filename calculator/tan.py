# tan.py

import math


__all__ = ["calc_tan"]


def calc_tan(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return math.tan(n)


def calc_d_tan(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return 1 / (math.cos(n)) * 1 / (math.cos(n))
