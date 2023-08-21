class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for child, par in adjacentPairs:
            graph[child].append(par)
            graph[par].append(child)
            indegree[child] += 1
            indegree[par] += 1
        
        
        queue = deque()
        end = []
        for node in indegree:
            if indegree[node] == 1:
                if queue:
                    end.append(node)
                    break
                    
                else:
                    queue.append(node)
                
                
        ans = []
        while queue:
            
            for _ in range(len(queue)):
                
                src = queue.popleft()
                ans.append(src)
                
                for child in graph[src]:
                    indegree[child] -= 1
                    
                    if indegree[child] == 1:
                        queue.append(child)
        ans.extend(end)
        return ans
        
        