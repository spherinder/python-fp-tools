from pymonad import *
from functools import reduce


def concat(xs):
    return sum(xs, [])
