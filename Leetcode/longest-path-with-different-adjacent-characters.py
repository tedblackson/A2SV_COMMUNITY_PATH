class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for child , par in  enumerate(parent):
            graph[par].append(child)
        
        ans = [0]
        def dfs(parent):
            
            

            res = []
            _max = 0
            flag = False
            for child in graph[parent]:
                temp = dfs(child)
                ans[0] = max(ans[0], temp)
                if s[child] != s[parent]:
                    _max = max(temp, _max)
                    flag = True
                    res.append((-1 * temp, child, s[child]))
                  
            heapify(res)
            tot = 1
            
            for i in range(2):
                if res:
                    tot += -1 * heappop(res)[0]
                    
            
                
            
            ans[0] = max(ans[0], _max , tot)
           
            if not flag:
                return 1
            else:
                return _max + 1
            
        dfs(0)
        return ans[0]
                
            
            
            
            
            
                