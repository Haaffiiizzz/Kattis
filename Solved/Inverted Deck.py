n = int(input())
numList = list(map(int, input().split()))

correct = sorted(numList)

if numList == correct:
    print(1, 1)
    quit()

i = 0
while i < n and numList[i] == correct[i]:
    i += 1

j = n - 1
while j >= 0 and numList[j] == correct[j]:
    j -= 1

if numList[:i] + numList[i:j+1][::-1] + numList[j+1:] == correct:
    print(i+1, j+1) 
else:
    print("impossible")
