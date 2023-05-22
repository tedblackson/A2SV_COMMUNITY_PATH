class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        self.rep = {(row, col) : (row, col) for row in range(n) for col in range(m)}
        self.size = {(row, col) : 1 for row in range(n) for col in range(m)}
        
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        
        moves = [[{1,4, 6}, {1, 3, 5}, {}, {}],
                 [{} ,{}, {2,3, 4}, {2, 5, 6}], 
                 [{1, 4, 6}, {}, {}, {2, 5, 6}],
                 [{}, {1, 3, 5}, {}, {2, 5, 6}],
                 [{1, 4, 6}, {}, {2, 3, 4}, {}],
                 [{}, {1, 3, 5}, {2, 3, 4}, {}]]
        
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        for row in range(n):
            for col in range(m):
                cnt = 0
                for direction in directions:
                    _row = row + direction[0]
                    _col = col + direction[1]
                    
                    if inBound(_row, _col) and grid[_row][_col] in moves[grid[row][col] - 1][cnt]:
                        self.union((row, col), (_row, _col))
                    cnt += 1
        
        if self.find((0, 0)) == self.find((n -1, m - 1)):
            return True
        return False
                    
    def union(self, x, y):
        
        xrep = self.find(x)
        yrep = self.find(y)
        
        if self.size[xrep] > self.size[yrep]:
            self.rep[yrep] = xrep
            self.size[xrep] += self.size[yrep]
        
        else:
            self.rep[xrep] = yrep
            self.size[yrep] += self.size[xrep]
    def find (self, x):
        
        if x == self.rep[x]:
            return x
        
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
            
        
                    
        

        
        
        
            
            