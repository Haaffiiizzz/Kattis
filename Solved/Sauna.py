n = int(input())

intervals = []
for i in range(n):
    interval = list(map(int, input().split(" ")))
    intervals.append(interval)

maxStart = max(interval[0] for interval in intervals)
minEnd = min(interval[1] for interval in intervals)

if maxStart > minEnd:
    print("bad news")

else:
    print(minEnd - maxStart + 1, maxStart)
