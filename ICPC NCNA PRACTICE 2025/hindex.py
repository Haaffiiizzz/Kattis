n = int(input())

nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)

for i in range(n):
    if nums[i] < i +1:
        print(i)
        break

else:
    print(n)