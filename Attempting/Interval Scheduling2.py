def to_min(s):
    h, m = map(int, s.split(":"))
    return h * 60 + m

def to_str(t):
    return f"{t // 60:02d}:{t % 60:02d}"

def feasible(k, orig, start, end):
    n = len(orig)
    intervals = []
    cur = start
    for i in range(n):
        Li, Ri = orig[i]
        Ai = max(cur, Li)  # cannot start before previous ends, must include Li
        Bi = max(Ri, Ai + k)  # must include Ri, and length >= k
        if Bi > end:  # past closing
            return False, []
        intervals.append([Ai, Bi])
        cur = Bi

    # if last doesn't reach end, we’ll try to shift backward
    if intervals[-1][1] < end:
        need = end - intervals[-1][1]
        for i in range(n - 1, -1, -1):
            max_shift = intervals[i][0] - (intervals[i - 1][1] if i > 0 else start)
            shift = min(max_shift, need)
            if shift > 0:
                intervals[i][0] -= shift
                intervals[i][1] -= shift
                need -= shift
            if need == 0:
                break
        if need > 0:
            return False, []

        # finally align last interval to end
        diff = end - intervals[-1][1]
        intervals[-1][1] += diff
        intervals[-1][0] += diff

    if intervals[-1][1] != end:
        return False, []
    return True, intervals

n = int(input())
orig = []
for _ in range(n):
    l, _, r = input().partition('-')
    orig.append((to_min(l.strip()), to_min(r.strip())))

start, end = orig[0][0], orig[-1][1]
low = max(R - L for L, R in orig)
high = end - start
best = orig[:]  # fallback

while low <= high:
    mid = (low + high) // 2
    ok, intervals = feasible(mid, orig, start, end)
    if ok:
        best = intervals
        low = mid + 1
    else:
        high = mid - 1
for a, b in best:
    print(f"{to_str(a)} - {to_str(b)}")