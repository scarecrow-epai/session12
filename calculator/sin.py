# sin.py

import math

__all__ = ["calc_sin"]


def calc_sin(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return math.sin(n)


def calc_d_sin(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    return math.cos(n)
