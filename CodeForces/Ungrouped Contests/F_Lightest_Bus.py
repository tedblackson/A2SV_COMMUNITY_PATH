from itertools import accumulate
N = int(input())

for _ in range(N):
    n = int(input())
    weights = list(map(int, input().split()))
    
    weights = list(accumulate(weights))
    weights.append(0)
    ans = weights[min(n - 1, 11)]
    
    for i in range(12, n , 6):
        ans = min(ans, weights[min(i + 11, n - 1)] - weights[i - 1])
        
    print(ans)
  
    
    