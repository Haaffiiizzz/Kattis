r, g, b = map(int, input().split())
c, d, e = map(int, input().split())

r, g, b = r-c, g-d, b-e

avrg, avgb = map(int, input().split())
bought = 0
if r > avrg:
    print(-1)
    quit()
elif r > 0:
        avrg = avrg - r
        bought += r

if b > avgb:
    print(-1)
    quit()

elif b > 0:
     avgb = avgb - b
     bought += b
    
if g > avrg + avgb:
     print(-1)
     quit()
elif g > 0:
    bought += g
print(bought)