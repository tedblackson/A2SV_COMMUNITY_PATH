class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for source, dest in dislikes:
            graph[source].append(dest)
            graph[dest].append(source)
        
        visited = {}
        
        def dfs(node, color):
            
            visited[node] = color
            
            for child in graph[node]:
                
                if child not in visited:
                    if not dfs(child,  not color):
                        return False
                elif visited[node] == visited[child]:
                    return False
            return True
        
        for node in range(1, n + 1):
            if node not in visited and not dfs(node, True):
                return False
        return True
    
            
        