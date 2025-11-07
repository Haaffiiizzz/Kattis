n = int(input())
nums = sorted(map(int, input().split()))
res = 0
i = 0

while i < n:
    res += nums[i]
    while i < n - 1 and nums[i] + 1 == nums[i + 1]:
        i += 1
    i += 1

print(res)