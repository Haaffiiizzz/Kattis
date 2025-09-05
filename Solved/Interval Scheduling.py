n = int(input())
intervals = []
maxNonOverlap = 1
for i in range(n):
    interval = list(map(int, input().split(" ")))
    intervals.append(interval)

intervals = sorted(intervals, key= lambda x: x[1])

prev = intervals[0]
for interval in intervals[1:]:
    if prev[0] < interval[1] and interval[0] < prev[1]:
        pass
    else:
        prev = interval
        maxNonOverlap += 1
print(maxNonOverlap)



