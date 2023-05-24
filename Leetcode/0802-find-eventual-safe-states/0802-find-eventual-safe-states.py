class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        order = []
        colors = [0] * len(graph)
        
     
        def dfs(node):
            
            if colors[node] == 1:
                return True
            
            colors[node] = 1
            
            for child in graph[node]:
                if colors[child] == 0 and dfs(child):
                    return True
                elif colors[child] == 1:
                    return True
                
            colors[node] = 2
            order.append(node) 
            return False
        
        
        for node in range(len(graph)):
            if colors[node] == 0:
                dfs(node)
            
        return sorted(order)
                
                    