class Solution:
    def totalNQueens(self, n: int) -> int:
  
        self.cnt = 0
        
        board = ["." * n for _ in range(n)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < n
        
        def isFree(row, col):
            
            
            for r, c in directions:
            
                _row , _col = row, col
                
                while inBound(_row, _col):
                   
                    if board[_row][_col] == "Q":
                        return False
                    _row += r
                    _col += c
            return True
            
        
            
        def dfs(row, board):
            if row == n:
                self.cnt += 1
                return
            
                
            
            for col in range(n):

                if isFree(row, col):
                
                    board[row] = "." * (col ) + "Q" + "." * (n - col - 1)
                    dfs(row + 1 , board)
                    board[row] =  "." * n
               
        dfs(0, board)
        
       
        return self.cnt
                    