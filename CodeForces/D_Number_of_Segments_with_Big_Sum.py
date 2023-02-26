import math
N , S = map(int, input().split())

arr = list(map(int, input().split()))


start = total = count =0
shortest = math.inf
for end in range(N):
    total += arr[end]

    while total - arr[start] >= S:
        total -= arr[start]
        start += 1
    
    if total >= S:
        count += start + 1
        
print(count)

        
    
    