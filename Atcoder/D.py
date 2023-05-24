from heapq import heapify, heappop, heappush
N , M, D = map(int, input().split())

Aoki = list(map(int, input().split()))
Aoki = [-1 * ele for ele in Aoki]
Snuke = list(map(int, input().split()))
Snuke = [- 1 * ele for ele in Snuke]

heapify(Aoki)
heapify(Snuke)

while Aoki and Snuke:
    
    one = heappop(Aoki)
    two = heappop(Snuke)
    if abs(one - two) <= D:
        print(-1 * (one + two) )
        exit()
    else:
        if one > two:
            heappush(Aoki, one)
            
        elif one < two:
            heappush(Snuke, two)
            
print(-1)
        


