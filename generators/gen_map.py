def adder(*n):
    return sum(n)
s1 = sum(map(lambda n: adder(*n), zip(range(100), range(1, 101))))
print ("Using map:", s1)
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print ("Using a generator:", s2)
