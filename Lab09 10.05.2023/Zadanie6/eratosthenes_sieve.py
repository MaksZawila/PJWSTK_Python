def eratosthenes_sieve(n=75):
    primes = []
    i = 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            yield i
        i += 1
