import math
N = int(input())
for _ in range(N):
    ans = math.inf
    
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        copy = arr.copy()
        for j in range(i + 1, n):
            copy[i] = copy[i] & copy[j]
            copy[j] = copy[i] & copy[j]
        ans = min(ans, min(copy))
    print(ans)
        
            
            