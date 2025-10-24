n, t = map(int, input().split())

# Bucket customers by their latest time (deadline)
buckets = [[] for _ in range(t)]
for _ in range(n):
    m, d = map(int, input().split())
    if d >= t:
        d = t - 1
    if d >= 0:
        buckets[d].append(m)

# Greedy: at each time, among all not-yet-served with deadline >= time,
# serve the one with the most money
import heapq
pq = []  # max-heap via negatives
ans = 0
for time in range(t - 1, -1, -1):
    for m in buckets[time]:
        heapq.heappush(pq, -m)
    if pq:
        ans -= heapq.heappop(pq)

print(ans)
