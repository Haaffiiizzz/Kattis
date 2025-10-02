a, b , c, d = map(int, input().split())
p, m , g = map(int, input().split())
word = {1: "one", 2: "both", 0: "none"}

count = 0
if p % (a + b) <= a and p % (a + b) != 0:
    count += 1
if p % (c + d) <= c and p % (c + d) != 0:
    count += 1

print(word[count])

count = 0
if m % (a + b) <= a and m % (a + b) != 0:
    count += 1
if m % (c + d) <= c and m % (c + d) != 0:
    count += 1
print(word[count])

count = 0
if g % (a + b) <= a and g % (a + b) != 0:
    count += 1
if g % (c + d) <= c and g % (c + d) != 0:
    count += 1
print(word[count])