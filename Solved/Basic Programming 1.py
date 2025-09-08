n, t = map(int, input().split())
a = list(map(int, input().split()))

if t == 1:
    print("7")

elif t == 2:
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] == a[1]:
        print("Equal")
    else:
        print("Smaller")

elif t == 3:
    new = sorted(a[:3])
    print(new[1])

elif t == 4:
    print(sum(a))

elif t == 5:
    print(sum(x for x in a if x % 2 == 0))

elif t == 6:
    print("".join(chr(97 + (x % 26)) for x in a))

else:
    visited = set()
    i = 0
    while True:

        if i >= n or i < 0:
            print("Out")
            break
        elif i == n - 1:

            print("Done")
            break
        if i in visited:
            print("Cyclic")
            break
        
        visited.add(i)
        i = a[i]


