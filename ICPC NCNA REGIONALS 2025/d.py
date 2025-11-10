n, k = map(int, input().split())
intMap = {i: 0 for i in range(24)}


for j in range(n):
    start, end = map(int, input().split())

    for i in range(start, end):
        intMap[i] += 1
res = 0
for value in intMap.values():
    if value >= k:
        res += 1
print(res)

    

