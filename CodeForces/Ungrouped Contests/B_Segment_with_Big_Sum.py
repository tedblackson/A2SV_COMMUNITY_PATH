import math
N , S = map(int, input().split())

arr = list(map(int, input().split()))


start = total = 0
shortest = math.inf
for end in range(N):
    total += arr[end]

    
    while total >= S:
        shortest = min(shortest, end - start + 1)
        total -= arr[start]
        start += 1
print(shortest) if shortest != math.inf else print(-1)
        
    
    