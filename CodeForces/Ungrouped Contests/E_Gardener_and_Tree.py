from collections import defaultdict, deque
    
N = int(input())

for _ in range(N):
    input()
    
    n, k = map(int, input().split())
    queue = deque()
    
    tree = defaultdict(list)
    indegree = [0] * (n + 1)
    
    if n <= 1:
        if k >= 1:
            print(0)
        else:
            print(n)
        break
    
  
    for _ in range(n -1):
        
        src, dest = map(int, input().split())
        
        tree[src].append(dest)
        tree[dest].append(src)
        indegree[src] += 1
        indegree[dest] += 1
    
    
    for node, val in enumerate(indegree):
        
        if val == 1:
            queue.append(node)
            
            
    removed = 0
    while k > 0 and queue:
        
        _lenq = len(queue)
        removed += _lenq
        
        for _ in range(_lenq):
            src = queue.popleft()
            
            for child in tree[src]:
                if child != src:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        queue.append(child)
        k -= 1  
        
    print(n - removed)
    
        
            
        
    
    
    