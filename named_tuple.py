from collections import namedtuple
Example = namedtuple('Example', ['a', 'b'])
example = Example('hing', 'nother hing')
print("A: " + example.a)
print("B: " + example.b)
