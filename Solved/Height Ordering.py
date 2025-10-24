n = int(input())

for i in range(n):
    data = list(map(int, input().split()))
    l, nums = data[0], data[1:]
    count = 0

    for k in range(1, len(nums)):
        curr = nums[k]
        j = k
        while j > 0 and nums[j-1] > curr:
            nums[j] = nums[j-1]
            j -= 1
            count += 1
        nums[j] = curr
    print(l, count)


