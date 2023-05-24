class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = {}
        
        
        def dfs(node, color):
            
            visited[node] = color
             
            for child in graph[node]:
                
                if child not in visited:
                    if not dfs(child, 0 if color == 1 else 1):
                        return False
                    
                if visited[node] == visited[child]:
                    return False
            return True
        
        
        for node in range(n):
            if node not in visited:
                if not dfs(node, 0):
                    return False
        return True
                
            