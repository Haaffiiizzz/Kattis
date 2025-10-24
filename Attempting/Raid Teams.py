from sys import stdin
n = int(input())
skill1 = {}
skill2 = {}
skill3 = {}

for i in range(n):
    player = input().split()
    skill1[player[0]] = int(player[1])
    skill2[player[0]] = int(player[2])
    skill3[player[0]] = int(player[3])

for _ in range(n//3):
    best1 = sorted(list(skill1.keys()), key= lambda x: (-skill1[x], x))[0]
    del skill1[best1]
    del skill2[best1]
    del skill3[best1]
    best2 = sorted(list(skill2.keys()), key= lambda x: (-skill2[x], x))[0]
    del skill1[best2]
    del skill2[best2]
    del skill3[best2]
    best3 = sorted(list(skill3.keys()), key= lambda x: (-skill3[x], x))[0]
    del skill1[best3]
    del skill2[best3]
    del skill3[best3]

    print(best1, best2, best3)

