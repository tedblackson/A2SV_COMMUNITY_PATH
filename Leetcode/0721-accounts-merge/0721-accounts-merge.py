class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        self.rep = [i for i in range(n)]
        self.rank = [1] * n
        unique = defaultdict(set)
        
        
        for i in range(n):
            first_account = accounts[i]
            for j in range(i + 1, n):
                second_account = accounts[j]
                
                if self.haveCommon(first_account, second_account):
                    self.union(i, j)
        
        for i in range(n):
            self.rep[i] = self.find(self.rep[i])
            key = (self.rep[i], accounts[i][0])
            for j in range(1, len(accounts[i])):
                ele = accounts[i][j]
        
                if ele not in unique[key]:
                    unique[key].add(ele)
        
        for key in unique:
            unique[key] = sorted(list(unique[key]))
        
        ans = []
        for key, val in unique.items():
            temp = [key[1]]
            temp += val
            ans.append(temp)
        return ans

                
                
        
        
        
        
    
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
                self.rank[xrep] += self.rank[yrep]
            
            else:
                self.rep[xrep] = yrep
                self.rank[yrep] += self.rank[xrep]
        
            
    def haveCommon(self, first, second):
        
        for i in range(1, len(first)):
                if first[i] in second:
                    return True
        return False
        