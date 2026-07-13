n = int(input())

nums = list(map(int, input().split()))
nums.sort()

total = 0

i = 0

while i < n:
    curr = nums[i]
    while i < n - 1 and nums[i] + 1 == nums[i + 1]:
        i += 1
    total += curr
    i += 1   

print(total)