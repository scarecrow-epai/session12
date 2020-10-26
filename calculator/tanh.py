# tanh.py

import math


__all__ = ["calc_tanh"]


def calc_tanh(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")

    return math.tanh(n)


def calc_d_tanh(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return 1 - (math.tanh(n) * math.tanh(n))
