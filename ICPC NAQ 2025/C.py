n , k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums = set(nums)
res = len(nums)
if res > k:
    print(k)
else:
    print(res)

