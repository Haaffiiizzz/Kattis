def to_min(s):
    h, m = map(int, s.split(":"))
    return h*60 + m

def to_str(t):
    return f"{t//60:02d}:{t%60:02d}"

n = int(input())
orig = []
for _ in range(n):
    l, _, r = input().partition('-')
    orig.append((to_min(l.strip()), to_min(r.strip())))

start, end = orig[0][0], orig[-1][1]
total = end - start
ideal = total // n

times = [start]
for i in range(1, n):
    # next boundary = at least orig[i-1][1], at most orig[i][0]
    nxt = max(times[-1] + ideal, orig[i-1][1])
    nxt = min(nxt, orig[i][0])
    times.append(nxt)
times.append(end)

for i in range(n):
    print(f"{to_str(times[i])} - {to_str(times[i+1])}")