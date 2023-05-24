from heapq import heapify, heappop, heappush
N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    
    whiteboards = list(map(int, input().split()))
    changes = list(map(int, input().split()))
    
    heapify(whiteboards)
    for i in range(m):
        heappop(whiteboards)
        val = changes[i]
        heappush(whiteboards, val )
    max_sum = sum(whiteboards) 
                
    print(max_sum)
    