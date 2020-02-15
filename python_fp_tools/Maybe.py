from typeclasses import Monoid, Monad
from abc import ABCMeta, abstractmethod


class Maybe(Monad, Monoid):

    def __init__(self, value):
        raise NotImplementedError("Can't create objects of \
        type Maybe: use Just(something) or Nothing.")

    def __eq__(self, other):
        if not isinstance(other, Maybe):
            raise TypeError("Can't compare two different types.")

    @staticmethod
    def unit(value):
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
        super().__eq__(other)
        if isinstance(other, _Nothing):
            return False
        elif (self.getValue() == other.getValue()):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

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
        super().__eq__(other)
        if isinstance(other, _Nothing):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    map, amap, bind = [lambda self, _: self] * 3

    def map(self, _):
        return self

    def amap(self, _):
        return self

    def bind(self, _):
        return self

    def plus(self, other):
        return other


Nothing = _Nothing()


class First(Monoid):
    def __init__(self, value):
        if not isinstance(value, Maybe):
            raise TypeError
        else:
            super().__init__(value)

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


class Last(Monoid):
    def __init__(self, value):
        if not isinstance(value, Maybe):
            raise TypeError
        else:
            super().__init__(value)

    def __str__(self):
        return str(self.value)

    @staticmethod
    def zero():
        return First(Nothing)

    def plus(self, other):
        if isinstance(other.value, Just):
            return other
        else:
            return self
