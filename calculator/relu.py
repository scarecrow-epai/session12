# relu.py

import math


__all__ = ["calc_relu"]


def calc_relu(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")

    return max(0, n)


def calc_d_relu(n):
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n should be a number.")
    if n > 0:
        return 1
    else:
        return 0
