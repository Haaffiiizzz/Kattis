first = tuple(map(int, input().split()))
second = tuple(map(int, input().split()))
third = tuple(map(int, input().split()))

x = (first[0] + second[0] + third[0])/3
y = (first[1] + second[1] + third[1])/3

print(x, y)