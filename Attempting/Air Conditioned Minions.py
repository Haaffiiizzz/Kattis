numMin = int(input())

intervals = {}
first = input().split(" ")
intervals[1] = [(int(first[0]), int(first[1]))]
i = 1

for _ in range(numMin - 1):
    data = input().split(" ")
    first = int(data[0])
    second = int(data[1])
    
    found = False
    for key, value in intervals.items():
        doable = True
        for tup in value:
            if not (second < tup[0] or first > tup[1]):
                doable = False
                break
        if doable:
            value.append((first, second))
            found = True
    if not found:
        i += 1
        intervals[i] = [(first, second)]

print(i)
            
    
#not solved yet
                
                
                
                
                
            

