import math
N = int(input())

for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    maxSum = 0
    curMax = arr[0]
    
    for right in range(1, len(arr)):  
        if arr[right - 1] * arr[right] > 0:
            curMax = max(curMax, arr[right])
        else:
            maxSum += curMax
            curMax = arr[right]
    maxSum += curMax
    print(maxSum)
            
        
        
        
        
        
        
    
        
