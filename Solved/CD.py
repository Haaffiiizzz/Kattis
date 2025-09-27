import sys
input = sys.stdin.read().splitlines()
idx = 0


while idx < len(input):
    n, m = map(int, input[idx].split())
    idx += 1
    print("idx", idx)
    if n == 0 and m == 0:
        break

    jack = list(input[idx:idx+n])
    idx += n

    jill = list(input[idx:idx+m])
    idx += m

    new = jack + jill
    print(len(new) - len(set(new)))

    
