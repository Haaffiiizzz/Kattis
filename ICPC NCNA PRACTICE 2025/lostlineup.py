n = int(input())
nums = list(map(int, input().split()))
newDict = {}
newNum = sorted(nums)
for i, el in enumerate(nums):
    newDict[el] = i
print("1", end=" ")
res = []
for i in newNum:
    res.append(str(newDict[i] + 2))

print(" ".join(res))