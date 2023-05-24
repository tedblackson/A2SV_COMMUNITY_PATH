class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        index = []
        queue = deque()
        indegree = [0] * n
        
        if n == 1:
            return [0]
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            indegree[src] += 1
            indegree[dest] += 1
            
        for node, val in enumerate(indegree):
            if val == 1:
                queue.append(node)
        
        while queue:
            _lenq = len(queue)
            if n <= 2:
                return list(queue)
            
            for i in range(_lenq):
                
                src = queue.popleft()
                
                for child in graph[src]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        queue.append(child)
            n -= _lenq
            
            
                
                

            
            
                
        
        
        
