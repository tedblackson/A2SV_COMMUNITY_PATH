class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        rows = len(matrix) 
        cols = len(matrix[0])
        self.matrice = [ [0] * (cols + 1) for r in range(rows + 1)]
        # print(self.matrice)
        
        for i in range(rows):
            prefix = 0
            for j in range (cols):
                prefix += matrix[i][j]
                above = self.matrice[i][j + 1]
                self.matrice[i +1][j + 1]  = prefix + above
        
        
        
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        bottomR = self.matrice[row2 + 1][col2 + 1]
        above = self.matrice[row1][col2 + 1]
        left = self.matrice[row2 + 1][col1]
        
        topLeft = self.matrice[row1][col1]
        
        return bottomR - above - left + topLeft
        
        
        
        
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)