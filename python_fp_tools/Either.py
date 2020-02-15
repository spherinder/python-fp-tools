from typeclasses import Monad


class Result(Monad):

    def __init__(self, value):
        raise NotImplementedError("You can not create objects of \
        type Result; use Success(something) or Error(something).")

    def __eq__(self, other):
        if not isinstance(other, Result):
            raise TypeError("Can not compare different types.")

    @staticmethod
    def unit(cls, value):
        return Success(value)


class Error(Result):
    def __init__(self, errorMsg):
        super(Result, self).__init__(errorMsg)

    def __eq__(self, other):
        super().__eq__(other)
        if not isinstance(other, Error):
            return False
        else:
            return self.getValue() == other.getValue()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "Error " + str(self.getValue())

    def fmap(self, _):
        return self

    def amap(self, _):
        return self

    def bind(self, _):
        return self


class Success(Result):

    def __init__(self, value):
        super(Result, self).__init__(value)

    def __eq__(self, other):
        super(Success, self).__eq__(other)
        if not isinstance(other, Success):
            return False
        elif (self.getValue() == other.getValue()):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "Success: " + str(self.getValue())

    def fmap(self, function):
        return Success(function(self.getValue()))

    def amap(self, functorValue):
        return functorValue.map(self.getValue())

    def bind(self, function):
        return function(self.getValue())
