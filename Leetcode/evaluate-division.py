class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        weights = defaultdict(float)
        graph = defaultdict(list)
        
        for i, (x, y) in enumerate(equations):
            graph[x].append(y)
            graph[y].append(x)
            weights[(x, y)] = values[i]
            weights[(y, x)] = 1 / values[i]
            
        
       
        def dfs(cur, prev, cost):
            
            
            
            if cur == y:
                final  = cost * weights[(prev, cur)]  
                if answer[i] != -1 and answer[i] != final:
                    answer[i] = False
                else:
                    answer[i] = final
                return
            
            for child in graph[cur]:
                if child not in visited:
                    visited.add(child)
                    curW = weights[(prev, cur)] if prev else  1
                    res = dfs(child, cur, cost * curW)
                    
                
                
        answer = [-1] * len(queries)
        for i, (x, y) in enumerate(queries):
            
            visited = {x,}
            
            if x == y and graph[x]:
                answer[i] = 1
            else:
                dfs(x, None, 1)
            
                answer[i] = -1 if answer[i] == 0  or answer[i] is False else answer[i]

                    
        return answer
            
            
                
            
                        
                        
                    
                
            
            
        