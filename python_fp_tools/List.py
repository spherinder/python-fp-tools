from typeclasses import Traversable, Monad
from functools import reduce
import builtins


def concat(xs):
    return xs.foldl(lambda a, b: a + b, xs[0].zero()) if xs else xs


def range(*args):
    return List(*builtins.range(*args))


def map(f, xs):
    return xs.map(f)


class List(list, Monad, Traversable):

    def __init__(self, *values):
        super().__init__(values)

    def __eq__(self, other):
        if not isinstance(other, List):
            raise TypeError("Can't compare List with non-List type.")
        return super().__eq__(other)

    def __ne__(self, other):
        if not isinstance(other, List):
            return True
        return super().__ne__(other)

    def __getslice__(self, start, end):
        return self.__getitem__(slice(start, end))

    def __getitem__(self, key):
        if isinstance(key, slice):
            return List(*super().__getitem__(key))
        return super().__getitem__(key)

    def getValue(self):
        return self

    def __str__(self):
        return "List[" + ", ".join(self.map(str)) + "]"

    def __add__(self, other):
        return self.plus(other)

    # Functor
    def map(self, function):
        return List(*builtins.map(function, self))

    # Applicative
    @staticmethod
    def unit(value):
        return List(value)

    def amap(self, functorValue):
        return concat(self.map(functorValue.map))

    # Monad
    def bind(self, f):
        return concat(self.map(f))

    # def __rmul__(self, function):
    #     return self.map(function)

    @staticmethod
    def zero():
        return List()

    def plus(self, other):
        return List(*(super().__add__(other)))

    def foldl(self, function, unit):
        return List(*reduce(function, self.getValue(), unit))

    def sequence(self):
        def liftedCons(start, x):
            return x.map(lambda a: lambda b: b + [a]).amap(start)
        return reduce(liftedCons, self, self[0].unit([]))

