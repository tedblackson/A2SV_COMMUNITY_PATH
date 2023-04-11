class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        
        def dfs(node):
            
            visited.add(node)            
            
            for neighbor , con in enumerate(isConnected[node]):
                if con and neighbor not in visited:
                    dfs(neighbor)
          
        ans = 0
        for row in range(len(isConnected)):
            if row not in visited:
                dfs(row)
                ans += 1
        return ans
                
                