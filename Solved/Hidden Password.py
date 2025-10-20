password, rest = input().split()
n = len(password)
m = len(rest)
found = True
j = 0

for i in range(n):
    move = False
    while j < m:
        if rest[j] == password[i]:
            move = True
            j += 1
            break
        if rest[j] in password[i+1:]:
            print("FAIL")
            quit()
        j += 1
    
    if not move:
        found = False
        break
if found:
    print("PASS")
else:
    print("FAIL")

    

