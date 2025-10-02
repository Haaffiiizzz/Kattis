nums = []
n = int(input())

for i in range(n):
    nums.append(int(input()))

nums.sort()


a = 0
b = 0
i = 0

while i < (n// 2) + 1:
    if b < a:
            b += nums[n - 1 - i]
            a += nums[i]

    else:
            a += nums[n - 1 - i]
            b += nums[i]
    
    i += 1

    


print(min(a,b), max(a,b))
    