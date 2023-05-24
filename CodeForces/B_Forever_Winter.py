from collections import defaultdict, Counter, deque
N = int(input())

for _ in range(N):
    graph = defaultdict(list)
    n, m = map(int, input().split())
    indegree = [0] * (n + 1)
    for _ in range(m):

        src, dest = map(int, input().split())
        
        graph[src].append(dest)
        graph[dest].append(src)     
        indegree[src] += 1
        indegree[dest] += 1
    queue = deque()
    visited = set()
    for i, val in enumerate(indegree):
        if val == 1:
            visited.add(i)
            queue.append(i)
    
    level = 0  
    x = 0
    y = 0
    levels = [0] * 3
    
    while queue:
        _lenq = len(queue)
        levels[level] = _lenq
        level += 1  
        for _ in range(_lenq):
            src = queue.popleft()
            visited.add(src)
            
            for child in graph[src]:
                indegree[child] -=1
                if child not in visited:
                    if indegree[child] == 1:
                        queue.append(child)
    y = levels[0] // levels[1]
    x = levels[1] // levels[2]

    print(x, y)
            
      
            
                        
        
    
    
        
    
        
       