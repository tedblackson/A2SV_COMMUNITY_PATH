N = int(input())

for _ in range(N):
    
    n = int(input())
    ans = 0
    
    arr = list(map(int, input().split()))

    arr.sort()
    
    if len(arr) == 1:
        print(arr[0])
    else:
        def evaluate(one, two):
            while one %2 == 0:
                one //= 2
                two *= 2
            return one, two, one + two
        res = 0
        
        for i in range(n):
            
            one = two  = []

            for j in range(n):
                if arr[j] %2 == 0:
                    one = (arr[j], j)
                    break
            for j in range(n - 1, -1 , -1):
                if one and one[1] != j :
                    two = (arr[j], j)
                    break
            if one and two:
                res1  = evaluate(one[0], two[0])
                res2 = evaluate(two[0], one[0])
                res = max(res1, res2, key= lambda ele: ele[2])
                arr[one[1]] = res[0]
                arr[two[1]] = res[1]

        ans = sum(arr)
        print(ans)
    
    
    