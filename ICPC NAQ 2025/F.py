def main():
    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]

    a.sort()


    S = [0.0] * (n + 1)
    S2 = [0.0] * (n + 1)
    for i in range(1, n + 1):
        S[i] = S[i - 1] + a[i - 1]
        S2[i] = S2[i - 1] + a[i - 1] * a[i - 1]

    best = float('inf')
    for l in range(n - k + 1):
        r = l + k
        s = S[r] - S[l]
        s2 = S2[r] - S2[l]
        bad = s2 - (s * s) / k
        if bad < best:
            best = bad


    if abs(best - round(best)) < 1e-9:
        print(int(round(best)))
    else:
        print(best)

if __name__ == "__main__":
    main()
