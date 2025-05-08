
first = int(input())
print("starting")

while first:
    firstList = []
    secondList = []
    res = [0] * first
    for i in range(first):
        firstList.append(int(input()))
    for i in range(first):
        secondList.append(int(input()))
    
    firstSorted = sorted(firstList)
    secondSorted = sorted(secondList)
    
    for i in range(first):
        res[firstList.index(firstSorted[i])] = secondSorted[i]
    for i in res:
        print(i)
    
    print(" ")
        
    
    
    first = int(input())