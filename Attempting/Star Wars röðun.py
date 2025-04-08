n = int(input())
numbers = list(input().split())
third = n // 3 

first_third = numbers[:third] 
middle_third = numbers[third:2*third] 
last_third = numbers[2*third:] 
res = middle_third + first_third + last_third
res = " ".join(res)

