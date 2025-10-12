MOD = 998244353

n, k = map(int, input().split())
m = 2 * k + 1
num = pow(2 * k, 2 * k, MOD)
den = pow(m, 2 * k, MOD)
ans = n % MOD
ans = ans * num % MOD
ans = ans * pow(den, MOD - 2, MOD) % MOD
print(ans)
