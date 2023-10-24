class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        
        graph = defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        
        visited = {0, }
        
        def dfs(root):
            
            
            ans = [0, 0]
            for child in graph[root]:
                if child not in visited:
                    visited.add(child)
                    res = dfs(child)
                    ans[0] += res[0]
                    ans[1] += res[1]
            
            ans[1] += values[root]
            
            if ans[1] % k == 0:
                ans[0] += 1
                ans[1] = 0
            return ans
        
        res = dfs(0)
        return res[0]
            
            
                