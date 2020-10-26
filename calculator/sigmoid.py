# sigmoid.py

import math


__all__ = ["calc_sigmoid"]


def calc_sigmoid(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return 1 / (1 + math.exp(-1 * n))


def calc_d_sigmoid(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return calc_sigmoid(n) * (1 - calc_sigmoid(n))
