from heapq import heapify, heappop, heappush
from collections import namedtuple
n , m = map(int, input().split())

dishes = list(map(int, input().split()))
costs = list(map(int, input().split()))
customers = []
order = namedtuple('order', ['type', 'amount'])
for _ in range(m):
    ele = tuple(map(int, input().split()))
    customers.append(order(ele[0], ele[1]))

cheap = namedtuple('cheap', ['cost', 'type'])

cheapest = []


for i, cost in enumerate(costs):
    cheapest.append(cheap(cost, i))
heapify(cheapest)




for order in customers:
    total = 0
    amount = order.amount
    
    if dishes[order.type - 1] >= amount:
            
            dishes[order.type - 1] -= amount
            
            total += amount * costs[order.type - 1]
            amount = 0
    elif dishes[order.type - 1] > 0:
            
            amount -= dishes[order.type - 1]
            total += dishes[order.type - 1] * costs[order.type - 1]
            dishes[order.type - 1] = 0
    while amount > 0:
        if not cheapest:
            total = 0
            break
        cheap = heappop(cheapest)
        if dishes[cheap.type] >= amount:
            dishes[cheap.type] -= amount
            total += cheap.cost * amount
            amount = 0
            if dishes[cheap.type] > 0:
                heappush( cheapest, cheap)
        else:
            amount -= dishes[cheap.type]
            
            total += dishes[cheap.type] * cheap.cost
            dishes[cheap.type] = 0
    print(total)
                    
                
                    
            
        

            
        
        
        
    