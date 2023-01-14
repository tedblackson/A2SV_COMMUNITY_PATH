class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colStart = 0
        for row in range (len(matrix)):
            for col in range(colStart, len(matrix[0])):
                
                matrix[row][col] , matrix[col][row] = matrix[col][row], matrix[row][col]
            matrix[row].reverse()
            colStart += 1
