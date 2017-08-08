primes = []
upto = 100
for n in range(2, upto + 1):
    is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)
