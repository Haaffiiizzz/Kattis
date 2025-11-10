MOD = 1000000007
e = int(input())
l = int(input())
r = int(input())

def sieve(l, r):

    primes = [True] * (r - l + 1)

    for p in range(l, int(r**0.5) + 1):
        if primes[l - p] == True:
            for i in range(p * p, r + 1, p):
                primes[i] = False

    return primes[l:]

   
primes = sieve(l, r)
res = 1
for i in range(r-l):
    if primes[i]:
        res *= (l+i) ** e

print(res%MOD)
