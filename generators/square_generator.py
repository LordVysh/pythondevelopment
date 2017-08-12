def get_squares(n):
    for x in range(n):
        yield x ** 2
print(list(get_squares(10)))
