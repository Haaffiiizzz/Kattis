n = int(input())

List = [int(input()) for _ in range(n)]
List = sorted(List)[::-1]

for i in range(0, n):
    if List[i] < i +1:
        print(i)
        break

else:
    print(n)