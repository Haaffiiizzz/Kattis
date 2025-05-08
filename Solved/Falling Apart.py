n = int(input())

List = list(map(int, input().split()))
new = sorted(List)
new = new[::-1]
a = 0
b = 0

for i in range(0, n, 2):
    a += new[i]
for i in range(1, n, 2):
    b += new[i]
print(a, b)