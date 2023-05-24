N = int(input())

for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    odd= False
    if arr[0] % 2:
        smallestOdd = arr[0]
        odd = True
    else:
        smallestOdd = float('inf')
    for i in range(1, n):
        
        if smallestOdd == float('inf') and arr[i] %2:
            smallestOdd = arr[i]
            
        if odd and arr[i] %2 == 0 and (arr[i] - smallestOdd) <=  0:
            print('NO')
            break
        elif not odd and arr[i] %2 == 1 and arr[i] - smallestOdd <= 0:
            print('NO')
            break
    else:
        print("YES")
        
        
        
                