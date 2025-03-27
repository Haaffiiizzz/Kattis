# first = input().split()
# n = int(first[0])
# minCost = int(first[1])
# second = list(map(int, input().split()))
# array = sorted(second)

# count = 1
# for i in range(1, n):
#     if array[i] + array[i-1] > minCost:
#         break
#     count += 1
    
# print(count)

#if you sort, keep on adding the prices in twos until it reaches the max. once it reaches, count how many you added

first = input().split()
n = int(first[0])
minCost = int(first[1])
second = list(map(int, input().split()))
array = sorted(second)
result = array[0]
count = 1
for i in array[1:]:
    result += i
    if result <= minCost:
        count += 1
        result = i
    else:
        break
print(count)
        
    