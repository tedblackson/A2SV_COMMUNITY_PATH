class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        uniqueBoxes = defaultdict(set)
        allBoxes = defaultdict(list)
        uniqueColumns = defaultdict(set)
        allColumns = defaultdict(list)
        uniqueRows = defaultdict(set)
        allRows = defaultdict(list)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    uniqueColumns[col].add(board[row][col])
                    allColumns[col].append(board[row][col])
                    uniqueRows[row].add(board[row][col])
                    allRows[row].append(board[row][col])
        
        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.':
                            allBoxes[(row, col)].append(board[i][j])
                            uniqueBoxes[(row, col)].add(board[i][j])
                if len(uniqueBoxes[(row,col)]) != len(allBoxes[(row,col)]):
                    return False
        
        for key in range(0, 9):
          
            
            if len(uniqueColumns[key]) != len(allColumns[key]):
                return False
            elif len(uniqueRows[key]) != len(allRows[key]):
                return False
        
    
        
        return True
                    
                
            
        