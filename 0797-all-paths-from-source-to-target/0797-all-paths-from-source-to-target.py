class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        
        def dfs(node, path):
            path.append(node)
            if node == n - 1:
                ans.append(path[:])
                return
                
            
            for child in  graph[node]:
                dfs(child, path)
                path.pop()
        dfs(0, [])
        return ans
            
                
                    
                    
                    
            