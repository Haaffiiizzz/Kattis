n, d = map(int, input().split())

nums = list(map(int, input().split()))

mapCount = {}
for num in nums:
    div = num // d
    if div in mapCount:
        mapCount[div] += 1
    else:
        mapCount[div] = 1


count = 0
for key, value in mapCount.items():
    num = value * (value-1) / 2 #num pairs
    count += num
print(int(count))
