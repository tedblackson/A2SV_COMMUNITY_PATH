class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        first_row = False
        first_col = False
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0 and row == col == 0:
                    first_row = True
                    first_col = True
                
                elif matrix[row][col] == 0:
                    if row == 0:
                        first_row = True
                    else:
                        matrix[row][0] = True
                    if col == 0:
                        first_col = True
                    else:
                        matrix[0][col] = True
                        
        for row in range(m -1, -1, -1):
            for col in range(n -1, -1, -1):
                if col == 0 and first_col:
                    matrix[row][col] = 0
                elif row == 0 and first_row:
                    matrix[row][col] = 0
                elif matrix[0][col] is True :
                    
                    matrix[row][col] = 0
                elif matrix[row][0] is True :

                    matrix[row][col] = 0
                    
                    
            