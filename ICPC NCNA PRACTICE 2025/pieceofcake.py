n, h, v = map(int, input().split())
res = max(h, n- h) * max(n-v, v) * 4
print(res)