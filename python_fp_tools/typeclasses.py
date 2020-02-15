from abc import abstractmethod, ABCMeta


class Container(object):

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value


class Functor(Container):

    def __init__(self, value):
        super().__init__(value)

    @abstractmethod
    def map(self, function):
        pass


class Applicative(Functor):

    def __init__(self, function):
        super().__init__(function)

    @abstractmethod
    def amap(self, functorValue):
        pass

    @staticmethod
    @abstractmethod
    def unit(cls, value):
        pass


class Monad(Applicative):

    def __init__(self, value):
        super().__init__(value)

    @abstractmethod
    def bind(self, function):
        pass

    def __rshift__(self, function):
        result = self.bind(function)
        if not isinstance(result, Monad):
            raise TypeError("Operator '>>' must return a Monad instance.")
        return result


class Semigroup(Container, metaclass=ABCMeta):

    def __init__(self, value):
        super().__init__(value)

    @abstractmethod
    def plus(self, other):
        pass

    def __add__(self, other):
        result = self.plus(other)
        if not isinstance(result, Semigroup):
            raise TypeError("Operator '+' must return a Semigroup instance.")


class Monoid(Semigroup, metaclass=ABCMeta):

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    @abstractmethod
    def zero():
        pass


class Foldable(Monoid, metaclass=ABCMeta):
    def __init__(self, value):
        super().__init__(value)

    @abstractmethod
    def foldl(self, function):
        pass


class Traversable(Applicative, Foldable, metaclass=ABCMeta):

    def __init__(self, value):
        # print("Trav", value)
        super().__init__(value)

    @abstractmethod
    def sequence(self):
        pass
