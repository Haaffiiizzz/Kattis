n = int(input())
m = int(input())

List = [0] * n
List[0] = 1

for i in range(1, m):
    List[i % n] += 1

for i in List:
    print("*"*i)