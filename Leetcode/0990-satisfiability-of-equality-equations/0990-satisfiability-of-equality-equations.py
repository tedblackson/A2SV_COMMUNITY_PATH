class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        self.rep = {chr(i) : chr(i) for i in range(97, 123)}
        self.rank = {chr(i) : 1 for i in range(97, 123)}
        
        for equation in equations:
            if equation[1:3] == "==":
                self.union(equation[0], equation[3])
        
        
        for equation in equations:
            first = self.find(equation[0])
            second = self.find(equation[3])
            if not self.checkResult(first, second , equation[1:3]):
                return False
        
        return True
            
    
    def checkResult(self, first, second, operator):
        result = first == second
     
        if (operator == "==" and not result) or (operator == "!=" and result):
            return False
        return True
       

        
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
        