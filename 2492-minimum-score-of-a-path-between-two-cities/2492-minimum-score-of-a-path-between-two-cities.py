class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        weights = defaultdict(int)
        visited = set()
        
        for src, dest , weight in roads:
            graph[src].append(dest)
            graph[dest].append(src)
            weights[(min(src, dest), max(src, dest))] = weight
        
        
        def dfs(root):
            
            for child in graph[root]:
                _min[0] = min(_min[0], weights[(min(root, child), max(root, child))])
                if child not in visited:
                    
                    visited.add(child)
                    dfs(child)
        
        
      
        _min = [float('inf')]
        visited.add(1)
        dfs(1)
        
        return _min[0]
                
                
                    
                    
                  
        
