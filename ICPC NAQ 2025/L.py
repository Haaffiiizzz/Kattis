input()
observations = [int(x.strip()) for x in input().strip().split()]
a = observations[0]//3
b = observations[1] - a - a
c = observations[-1]//3
print( a, b, c )