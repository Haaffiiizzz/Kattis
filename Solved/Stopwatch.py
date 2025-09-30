n = int(input())
if n % 2 != 0:
    print("still running")
    quit()
total = 0
for i in range(0, n, 2):
    current = int(input())
    next = int(input())
    total += next - current
print(total)
