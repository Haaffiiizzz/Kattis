import sys

data = sys.stdin.read().strip().split()
it = iter(data)

while True:
    try:
        A = float(next(it))
        B = float(next(it))
    except StopIteration:
        break

    n = int(next(it))
    intervals = []
    for i in range(n):
        l = float(next(it))
        r = float(next(it))
        intervals.append((l, r, i))

    intervals.sort(key=lambda x: (x[0], -x[1]))

    # Special case: single point interval
    if A == B:
        chosen = None
        for l, r, idx in intervals:
            if l <= A <= r:
                chosen = idx
                break
        if chosen is None:
            print("impossible")
        else:
            print(1)
            print(chosen)
        continue

    result = []
    current = A
    idx = 0
    possible = True

    while current < B:
        best = None
        while idx < n and intervals[idx][0] <= current:
            if best is None or intervals[idx][1] > best[1]:
                best = intervals[idx]
            idx += 1
        if not best or best[1] <= current:
            possible = False
            break
        result.append(best[2])
        current = best[1]

    if not possible:
        print("impossible")
    else:
        print(len(result))
        print(" ".join(map(str, result)))
