from heapq import heappush , heappop , heapify
N = int(input())

for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr = [[-1 *ele, idx] for idx, ele in enumerate(arr)]
    heapify(arr)
    output = []
    while len(arr) > 1:
        val1 = heappop(arr)
        val2 = heappop(arr)
        if val1[0] and val2[0]:
            output.append([val1[1] + 1, val2[1] +1 ])
            
            val1[0] += 1 
            val2[0] += 1
            if val1 != 0:
                heappush(arr, val1)
            if val2 != 0:
                heappush(arr, val2)
            
    print(len(output))
    for ele in output:
        print(*ele)
        
        
    
        