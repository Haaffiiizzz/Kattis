n = int(input())
you = input()
m = len(you)
him = input()

if you == him:
    print(n)

else:
    diff = 0
    for i in range(m):
        if you[i] != him[i]:
            diff += 1
    
    if diff == m:# if you differ in all
        print(m - n)
    
    else:
        print(max(m - diff, n + diff))
