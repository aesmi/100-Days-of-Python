def prime_gen(n):
    primes = [2]
    # start at 3 because 2 is already in the list
    nextPrime = 3
    while nextPrime < n:
        isPrime = True
        i = 0
        squareRoot = int(nextPrime ** .5)
        while primes[i] <= squareRoot:
            if nextPrime % primes[i] == 0:
                isPrime = False
            i += 1
        if isPrime:
            primes.append(nextPrime)
        # Only checking for odd numbers so add 2
        nextPrime += 2
    print primes
print(prime_generator(255))