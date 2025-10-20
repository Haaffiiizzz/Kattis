n = int(input())
nums = list(map(int, input().split()))

add = 0
for i in nums:
    if i == -1:
        n -= 1
        continue
    elif i == 0:
        continue
    else:
        add += i
print(add/n)
