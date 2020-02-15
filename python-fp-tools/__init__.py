from functools import reduce
import operator as op
import builtins
from typeclasses import (
    Monad,
    Monoid,
    Traversable,
    Container
)


def concat(xs):
    return sum(xs, [])


class Maybe(Monad):

    def __init__(self, value):
        raise NotImplementedError("Can't create \
        objects of type Maybe: use Just(something) or Nothing.")

    def __eq__(self, other):
        if not isinstance(other, Maybe):
            raise TypeError("Can't compare two different types.")

    @staticmethod
    def of(value):
        return Just(value)

    @staticmethod
    def zero():
        return Nothing


class Just(Maybe):

    def __init__(self, value):
        super(Maybe, self).__init__(value)

    def __str__(self):
        return "Just " + str(self.getValue())

    def __eq__(self, other):
        super(Just, self).__eq__(other)
        if isinstance(other, _Nothing):
            return False
        elif (self.getValue() == other.getValue()):
            return True
        else:
            return False

    def map(self, function):
        return Just(function(self.getValue()))

    def amap(self, functorValue):
        return functorValue.map(self.getValue())

    def bind(self, function):
        return function(self.getValue())

    def plus(self, other):
        if other == Nothing:
            return self
        else:
            return Just(self.value + other.value)


class _Nothing(Maybe):
    def __init__(self, value=None):
        super(Maybe, self).__init__(value)

    def __str__(self):
        return "Nothing"

    def __eq__(self, other):
        super(_Nothing, self).__eq__(other)
        if isinstance(other, _Nothing):
            return True
        else:
            return False

    def map(self, _):
        return self

    def amap(self, _):
        return self

    def bind(self, _):
        return self

    def plus(self, other):

        return other


Nothing = _Nothing()


class First:

    def __init__(self, value):
        if not isinstance(value, Maybe):
            raise TypeError
        else:
            super(First, self).__init__(value)

    def __str__(self):
        return str(self.value)

    @staticmethod
    def zero():
        return First(Nothing)

    def plus(self, other):
        if isinstance(self.value, Just):
            return self
        else:
            return other


class List(list, Monad, Traversable):

    def __init__(self, *values):
        print(values)
        super(List, self).__init__(values)
        print(self.value)

    def __eq__(self, other):
        if not isinstance(other, List):
            raise TypeError("Can't compare List with non-List type.")
        return super().__eq__(other)

    def __ne__(self, other):
        if not isinstance(other, List):
            return True
        return super().__ne__(other)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return List(*super(List, self).__getitem__(key))
        return super(List, self).__getitem__(key)

    def __str__(self):
        return "[" + ", ".join(self.map(str)) + "]"

    @staticmethod
    def of(value):
        return List(value)

    def map(self, function):
        return List(*list(map(function, self)))

    def amap(self, functorValue):
        result = []
        for func in self.getValue():
            result.extend(functorValue.map(func))
        return List(*result)

    def bind(self, function):
        result = []
        for subList in (map(function, self)):
            result.extend(subList)
        return List(*result)

    @staticmethod
    def zero():
        return List()

    def plus(self, other):
        return List(*(super(List, self).__add__(other)))

    def sequence(self):
        def liftedCons(start, x):
            return x.map(lambda a: lambda b: b + [a]).amap(start)
        return reduce(liftedCons, self, self[0].of([]))



# a =List(List(2, 3, 4), List(8,7,6))
a = List(1,2,3)

print("a.getValue()", a.getValue())
print(a.sequence())
