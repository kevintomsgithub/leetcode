def countPrimes(n):
    primes = {}
    for i in range(2, n+1):
        primes[i] = True
    for i in range(2, int(n**(0.5))+1):
        if primes[i]:
            for x in range(i+1, n+1):
                if x%i == 0: primes[x]=False
    print(primes)
    count = 0
    for i in range(2, n+1):
        if primes[i] == True: count+=1
    return count

n = 10
print(countPrimes(n))