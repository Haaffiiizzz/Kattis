from bisect import bisect_left
import sys

input = sys.stdin.readline

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)

def solve():
    n = int(input().strip())
    rects = []
    ys = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        rects.append((x1, y1, x2, y2))
        ys.extend([y1, y2])

    # Coordinate compression for y
    ys = sorted(set(ys))
    def compress(y):
        return bisect_left(ys, y) + 1

    events = []
    for x1, y1, x2, y2 in rects:
        cy1, cy2 = compress(y1), compress(y2)
        # Horizontal edges
        events.append((x1, 2, 'add', cy1))
        events.append((x1, 2, 'add', cy2))
        events.append((x2, 0, 'remove', cy1))
        events.append((x2, 0, 'remove', cy2))
        # Vertical edges
        events.append((x1, 1, 'query', (cy1, cy2)))
        events.append((x2, 1, 'query', (cy1, cy2)))

    # Sort events by (x, priority) -> remove(0), query(1), add(2)
    events.sort()

    bit = Fenwick(len(ys))

    for _, _, typ, val in events:
        if typ == 'add':
            bit.update(val, 1)
        elif typ == 'remove':
            bit.update(val, -1)
        else:  # query
            l, r = val
            if bit.range_query(l, r) > 0:
                print(1)
                return
    print(0)

if __name__ == "__main__":
    solve()
