class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        ans = 1
        
        for i in range(n):
            detonate = bombs[i]
            for j in range(n):
                planted = bombs[j]
                
                hor = (detonate[0] - planted[0]) ** 2
                ver = (detonate[1] - planted[1])** 2
                distance = (hor + ver) ** 0.5
                _range = detonate[2]
                
                if i != j and  distance <= _range:
                    graph[i].append(j)
            
        
        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
        
        for node in range(n):
            visited = set()
            dfs(node)
            ans = max(ans, len(visited))
        return ans
            
            