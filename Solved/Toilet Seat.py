s = input().strip()


cnt1 = 0
seat = s[0]
for want in s[1:]:
    if seat != want:
        cnt1 += 1  
    if want != 'U':
        cnt1 += 1
    seat = 'U'


cnt2 = 0
seat = s[0]
for want in s[1:]:
    if seat != want:
        cnt2 += 1  
    if want != 'D':
        cnt2 += 1 
    seat = 'D'


cnt3 = 0
seat = s[0]
for want in s[1:]:
    if seat != want:
        cnt3 += 1
    seat = want

print(cnt1)
print(cnt2)
print(cnt3)

