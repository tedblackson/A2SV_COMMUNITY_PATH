class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        directions = [[0,1 ] , [1, 0]]
        
        
        memo = defaultdict(int)
        memo[(m-1, n - 2)] = 1
        memo[(m- 2, n - 1)] = 1
        
        if m == n == 1:
            return 1
        def inBound(row, col):
            
            return 0 <= row < m and 0 <= col < n
        
        

        def dfs(row, col):
            
           
            

            for direction in directions:
                
                _row = direction[0] + row
                _col = direction[1] + col
                
                if inBound(_row, _col):
                    if (_row, _col) not in memo:
                        dfs(_row, _col)
                        
                    memo[(row, col)] += memo[(_row, _col)]
                    
                    
            return memo[(row, col)]
        
        return dfs(0, 0)
            
            