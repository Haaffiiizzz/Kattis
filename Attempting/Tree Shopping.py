line = input().split()

n = int(line[0])
numTrees = int(line[1])


array = list(map(int, input().split()))

i = 0
small = float("inf")
while i < n - numTrees + 1:
    sub = array[i:i+numTrees]
    small = min(small, max(sub) - min(sub))
    i += numTrees - 1

print(small)
    
    