class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph  = [[] for _ in range(n)]
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        
        def dfs(root):
            if root == dest:
                return True
            for child in graph[root]:
                if child not in visited:
                    visited.add(child)
                    
                    if dfs(child):
                        freq[child] += 1
                        return True
        @cache
        def dp(node):
            halved = (price[node]*freq[node])/2
            notHalved = price[node]*freq[node]
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    one,zero = dp(n)
                    halved +=zero
                    notHalved +=min(one,zero)
            return halved, notHalved
        
        
        freq = [0 ] * n
        
        for src, dest in trips:
            visited = {src,}
            freq[src] += 1
            dfs(src)
        
        visited = {0,}
        ans = int(min(dp(0)))
        
        
        
        
        return ans

        
