N = int(input())

for _ in range(N):
    
    n = int(input())
    ans = 0
    
    arr = list(map(int, input().split()))
    op = 0
    for i in range(n):
        temp = arr[i]
        while temp %2 == 0:
            temp//=2
            op += 1
        arr[i] = temp
    ans = max(arr) * (2 ** op) + (sum(arr) - max(arr))
    

    print(ans)
    
    
    