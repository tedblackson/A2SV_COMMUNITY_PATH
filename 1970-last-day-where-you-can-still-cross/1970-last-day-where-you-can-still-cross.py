class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        
        def inBound(row, col):
            return 0 < row <= m and 0 < col <= n
        
        def dfs(row , col):
            if row == m :
                return True
            
            mat[row][col] = 2
            
            for _r, _c in directions:
                
                _row = row + _r
                _col = col + _c
         
                
                if inBound(_row, _col) and mat[_row][_col] == 0 and dfs(_row, _col):
                    return True
                
            return False
        
        
        left , right = 1 , m * n
     
        
        while left < right:
            
            mat = [[0] * (n + 1) for _ in range(m + 1)]
            
            mid = right - (right - left)//2
            
            
            for r, c in cells[:mid]:
                mat[r][c] = 1
            
            for i in range(1, n + 1):

                if mat[1][i] == 0 and dfs(1, i):
                    left = mid
                    break
            else:
                right = mid - 1
                
           
                
        return left
        
        
        
                
                
                
            
            
            
            