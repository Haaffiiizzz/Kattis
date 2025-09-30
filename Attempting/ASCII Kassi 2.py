n = int(input())
if n == 0:
    print( " x")
    print( "x x")
    print(" x")
else:
    print(" " * n + "x" + " " * n)


    for i in range(1, n + 1):
        print(" " * (n - i) + "/" + " " * (2 * i - 1) + "\\" + " " * (n - i))


    print("x" + " " * (2 * n - 1) + "x")


    for i in range(n, 0, -1):
        print(" " * (n - i) + "\\" + " " * (2 * i - 1) + "/" + " " * (n - i))


    print(" " * n + "x" + " " * n)
