class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.rep = [i for i in range(n + 1)]
        self.rank  = [1] * (n + 1)
        self.ans = []
        
        for src , dest in edges:
            self.union(src, dest)
        return self.ans
            
        
    def find(self, x):
        
        if x == self.rep[x]:
            return x
        
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    
    def union(self, x, y):
        
        xrep = self.find(x)
        yrep = self.find(y)
        
        if xrep != yrep:
            
            if self.rank[xrep] > self.rank[yrep]:
                self.rep[yrep] = xrep
            
            elif self.rank[xrep] < self.rank[yrep]:
                self.rep[xrep] = yrep
                
            else:
                self.rep[yrep] = xrep
                self.rank[xrep] += 1
        else:
            self.ans = [x, y]
            
            