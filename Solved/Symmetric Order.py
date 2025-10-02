
n = int(input())
x = 1
while n != 0:
    words = [input() for i in range(n)]
    
    first = []
    second = []

    for i in range(n):
        if i % 2 == 0:
            first.append(words[i])
        else:
            second.append(words[i])
    
    print("SET", x)
    for j in first:
        print(j)
    for j in second[::-1]:
        print(j)
    x += 1
    n = int(input())