n = int(input())

totalC = 0
totalM = 0
totalH = 0

for _ in range(n):

    curr = input().split(" ")
    if curr[0] == "J":
        totalC += 1
    if curr[1] == "J":
        totalM += 1
    if curr[2] == "J":
        totalH += 1

    
print(min(totalH, totalC, totalM))
    