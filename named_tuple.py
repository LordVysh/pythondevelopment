from collections import namedtuple
Example = namedtuple('Example', ['a', 'c', 'b'])
example = Example('hing', 'yet another hing', 'nother hing')
print("A: " + example.a)
print("B: " + example.b)
print("C: " + example.c)
print("Arbitrary change")
