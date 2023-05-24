class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1],[1, 1], [-1, -1], [1, -1], [-1, 1]]
        visited = set()
        visited.add(tuple(click))
        def count_mines(row, col):
            count = 0
            for direction in directions:
                _row = direction[0] + row
                _col = direction[1] + col
                if inBound(_row, _col) and board[_row][_col] == "M"  or board[row][col] == "X":
                    count += 1
            return count
            
        def inBound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        def dfs(row, col):
                       
            count = count_mines(row, col)
            if count == 0:
                board[row][col] = "B"
            else:
                board[row][col] = str(count)
                return
                
            for direction in directions:
                _row = direction[0] + row
                _col = direction[1] + col
                
                if inBound(_row, _col) and (_row, _col) not in visited:      
                    visited.add((_row, _col))
                    dfs(_row, _col)

        dfs(click[0], click[1])
        return board
            
            
            
            