# log.py

import math


__all__ = ["calc_log"]


def calc_log(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return math.log(n)


def calc_d_log(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return 1 / n
