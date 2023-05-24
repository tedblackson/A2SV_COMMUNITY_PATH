from collections import defaultdict, Counter
n , m = map(int, input().split())

graph = defaultdict(list)
rank = [1] * (n + 1)
rep = [i for i in range(n + 1)]


def find(x):
        
        if x == rep[x]:
            return x
        
        rep[x] = find(rep[x])
        return rep[x]
    
    
def union(x, y):
    
    xrep = find(x)
    yrep = find(y)
    
    if xrep != yrep:
        if rank[xrep] > rank[yrep]:
            rep[yrep] = xrep
            rank[xrep] += rank[yrep]
        
        else:
            rep[xrep] = yrep
            rank[yrep] += rank[xrep]
        
        return True
    return False

def main():
    for _ in range(m):

        group = list(map(int, input().split()))

        for i in range(1, group[0]):
            union(group[i] , group[i + 1])
    
    
    for i in range(n + 1):
        rep[i] = find(rep[i])
    
    counted = Counter(rep)
    
    ans = []
    for node in range(1, n + 1):
        ans.append(counted[rep[node]])
    print(*ans)

main()
        
    
    