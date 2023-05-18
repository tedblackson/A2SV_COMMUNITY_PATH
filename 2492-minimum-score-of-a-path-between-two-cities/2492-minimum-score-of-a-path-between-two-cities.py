class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        self.rep = [i for i in range(n + 1)]
        self.rank = [1] *(n + 1)
        
        
        for x, y , _ in roads:
            self.union(x, y)
            
        ans = float('inf')
        
        for x, y , weight in roads:
            if self.find(x) == self.find(y) == self.find(1):
                ans = min(ans, weight )
        return ans
                
        
        
    def find(self, x):
        
        if x == self.rep[x]:
            return x
        
        self.rep[x] = self.find(self.rep[x])
        
        return self.rep[x]
        
        
    def union(self, x, y):
        
        xrep = self.find(x)
        yrep = self.find(y)
        
        if self.rank[xrep] > self.rank[yrep]:
            self.rep[yrep] = xrep
        elif self.rank[xrep] < self.rank[yrep]:
            self.rep[xrep] = yrep
        
        else:
            self.rep[yrep] = xrep
            self.rank[xrep] += 1
        
        
        

                
                
                    
                    
                  
        
