N = int(input())


for _ in range(N):
    n  = int(input())
    arr = list(map(int, input().split()))
    
    flag = False
    ans = 0
    for ele in arr[:n -1]:
        
        if not flag and ele != 0:
          flag = True
        ans += ele if ele != 0 else 1 if flag else 0
    print(ans)
        
    
    