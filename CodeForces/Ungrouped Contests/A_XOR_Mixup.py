N = int(input())

for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    
    x = arr[0]
    
    # for i in range(1, n  - 1):
    #     x ^= arr[i]
    print(arr[-1])        