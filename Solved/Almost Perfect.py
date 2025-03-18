from sys import stdin
import math

for line in stdin:
    num = int(line)
    if num == 1:
        print(num, "not perfect")
        continue

    sum = 1
    r = int(math.sqrt(num))
    
    for i in range(2, r + 1):
        if num % i == 0:
            sum += i
            other = num // i
            if other != i:
                sum += other

    if sum == num:
        print(num, "perfect")
    elif sum < num - 2 or sum > num + 2:
        print(num, "not perfect")
    else:
        print(num, "almost perfect")
        
#Up until the square root of the number, find all divisors of the number. If b can divide a, then a//b can divide a too.
#THerefore we can use that to find all divisors without having to manually loop through the whole thing. Sum all divisors and just check
#if it meets the conditions