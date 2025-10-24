n, q = map(int, input().split())

# Fenwick Tree for fast range sums on stored bits
class BIT:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def add(self, i, delta):
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)

total = 0                # number of 1s in actual state
cakes = [0] * n          # stored bits (before global flip)
bit = BIT(n)             # sums over stored bits
flip = 0                 # global flip flag (0/1)

for _ in range(q):
    s = list(map(int, input().split()))
    t = s[0]
    if t == 1:
        i = s[1] - 1
        # actual value before toggle
        actual = cakes[i] ^ flip
        if actual == 1:
            total -= 1
        else:
            total += 1
        # toggle stored bit and update BIT
        old = cakes[i]
        cakes[i] ^= 1
        delta = 1 if old == 0 else -1
        bit.add(i+1, delta)
    elif t == 2:
        flip ^= 1
        total = n - total
    elif t == 3:
        print(total)
    elif t == 4:
        l, r = s[1], s[2]
        # convert to 1-based inclusive indices for BIT
        l1, r1 = l, r
        stored_ones = bit.range_sum(l1, r1)
        length = r1 - l1 + 1
        actual_ones = stored_ones if flip == 0 else (length - stored_ones)
        print(actual_ones)
    
