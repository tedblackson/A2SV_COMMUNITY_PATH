N = int(input())

for _ in range(N):
    
    n, k  = map(int, input().split())
    
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    arr1 = [(ele, i) for i , ele in enumerate(arr1)]
    temp = {}

    arr1.sort()

    arr2.sort()
    
    for one, two in zip(arr1, arr2):
        temp[one[1]] = two

    ans = []
    
    for i in range(n):
        ans.append(temp[i])
        
    print(*ans)
        
    