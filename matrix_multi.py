def matrix_mul(a, b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)]
            for r in a]

a = [[1, 2], [2, 1]]
b = [[3, 4], [4, 3]]
c = matrix_mul(a, b)
print(c)
