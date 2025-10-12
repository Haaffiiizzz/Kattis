import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))

s.sort(reverse=True)

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + s[i - 1]

best = 0.0

for k in range(1, n + 1):
    avg = (prefix[k] + a[k - 1]) / k
    if avg > best:
        best = avg

print(best)
