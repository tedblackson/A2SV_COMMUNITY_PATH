class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set()  for _ in range(n)]
        indegree = [0] * n
        
        queue = deque()
        graph = defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            indegree[dest] += 1
            
            
        for node, val in enumerate(indegree):
            
            if not val:
                queue.append(node)
        
        
        while queue:
            
            src = queue.popleft()
            
            for child in graph[src]:
                
                indegree[child] -= 1
                
                ans[child].add(src)
                ans[child] = ans[child].union(ans[src])
                
                if not indegree[child]:
                    queue.append(child)
        ans = [list(sorted(ele)) for ele in ans]
        return ans
                
                
            
        
            
            
            
            
            