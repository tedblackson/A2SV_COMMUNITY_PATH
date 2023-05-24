N = int(input())

for _ in range(N):
    n = int(input())
    
    arr = [i for i in range(1, n + 1)]
    
    _sum = sum(arr)
    
    arr[0] += _sum %n
    
    print(*arr)