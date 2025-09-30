n = int(input())

def tilings(n: int) -> int:
    
    if n % 2 == 1:
        return 0
    
    m = n // 2 
    
    if m == 0:
        return 1
    if m == 1:
        return 3
    
    T_prev2, T_prev1 = 1, 3
    for _ in range(2, m+1):
        T_curr = 4 * T_prev1 - T_prev2
        T_prev2, T_prev1 = T_prev1, T_curr
    
    return T_prev1

while n != -1:
    print(tilings(n))
    n = int(input())
