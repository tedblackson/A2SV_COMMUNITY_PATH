class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[1, 0], [-1, 0], [0, 1] , [0, -1]]
        visited = set()
        
        def inBound(row, col):
            return  0 <= row < len(board) and 0 <= col < len(board[0])
        def dfs(row, col):
            
            
            for direction in directions:
                _row = direction[0] + row
                _col = direction[1] + col
                
                if inBound(_row, _col) and board[_row][_col] == "O" and (_row, _col) not in visited:
                    visited.add((_row, _col))
                    dfs(_row, _col)
           
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                cond1 = row * col == 0
                cond2 = row == len(board) -1 or col == len(board[0]) - 1
                if cond1 or cond2:
                    if board[row][col] == "O" and (row, col) not in visited:
                        visited.add((row, col))
                        dfs(row, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"
        
        
        
        