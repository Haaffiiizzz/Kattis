nums = list(map(int, input().split()))

if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
    area = nums[0] * nums[1] * 0.5
    if area.is_integer():
        print(int(area))
    else:
        print(area)
else:
    print(-1)