nums = int(input())

while nums != -1:
    distance = 0
    distances = []
    
    for i in range(nums):
        line = input().split(" ")
        distances.append((int(line[0]), int(line[1])))
    distance += distances[0][0] * distances[0][1]
    
    for i in range(1, len(distances)):
        time = distances[i][1] - distances[i-1][1]
        distance += time * distances[i][0]
        
    print(distance, "miles")
    nums = int(input())
        
    
#solved!!
# Trick is for each set of values, store a tuple of the speed and time in a list. And then for 
# each tuple in the list, except the first one, the time taken is the time in that tuple minus the time in the previous tuple. Just multiply
#that to the speed and add to the overall distance