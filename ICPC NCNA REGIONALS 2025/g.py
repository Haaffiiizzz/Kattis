n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
k = int(input())

while k >= 0:

    while len(set(nums)) != len(nums):
        numsSet = set()
        for num in nums:
            if num in numsSet:
                numsSet.remove(num)
                nums.remove(num)
                nums.remove(num)
                nums.append(num + 1)
            else:
                numsSet.add(num)
    if k > 0:
        nums.extend([0, 0, 0])
    k -= 1
nums.sort()
for i in nums:
    print(i, end=" ")







