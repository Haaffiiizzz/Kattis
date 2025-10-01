n = int(input())

nums = list(map(float, input().split()))

total = sum(i ** 3 for i in nums)

import math
result = math.pow(total, 1/3)
print(f"{result:.6f}")