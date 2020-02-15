from collections import namedtuple
from List import List, concat, range
from functools import reduce


a = List(2,3,4)
b = List(9,7,5)
c = List(a, b)
f = lambda x: range(x)

t,r,e = [(lambda x, y: x)] * 3

if List(2):
    print(2)

print((lambda x: x+1, a))

print(a + b)
print("range", range(10))
print("bind", a.bind(lambda x: range(x)))
print("sequence", c.sequence())
print("slicing", List(2,3,5,6,7,3)[2:6])


