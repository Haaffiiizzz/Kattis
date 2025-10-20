n = int(input())

names = [input() for _ in range(n)]
up = False
down = False
i = 2
first = names[0]
curr = names[1]
dir = None
if first > curr:
    down = True
else:
    up = True

while i < n:
    next = names[i]
    if next > curr:
        up = True
    else:
        down = True
    curr = next
    i += 1

if up == down:
    print("NEITHER")
elif up:
    print("INCREASING")
else:
    print("DECREASING")


    
