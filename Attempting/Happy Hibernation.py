n, h, t = map(int, input().split())
nums = list(map(int, input().split()))

index = None

l = 0
r = 0
while r < len(nums):
    while r < len(nums) and nums[r] <= t:
        r += 1

    if r - l >= h:
        index = l
        break

    r += 1
    l = r
if index is None:
    print("Too hot!")
else:

    print(index)
