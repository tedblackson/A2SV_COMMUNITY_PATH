class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        
        for row in range(0, len(grid) - 2):
            allBox = []
            uniqueBox = set()
            for col in range(0, len(grid[0]) - 2):
                allBox = [
                    grid[row][col], grid[row + 1][col] , grid[row + 2][col],
                    grid[row ][col + 1] , grid[row + 1][col + 1] , grid[row + 2][col + 1],
                    grid[row][col + 2] , grid[row + 1][col + 2] , grid[row + 2][col + 2]
                         ]
                uniqueBox = list(filter(lambda x : x <=9 and x>=1 , allBox))
                uniqueBox = set(uniqueBox)
                rowSum1 = sum(grid[row][col: col + 3])
                rowSum2 = sum(grid[row + 1][col: col + 3])
                rowSum3 = sum(grid[row + 2][col: col + 3])
                
                rowEqual = rowSum1 == rowSum2 == rowSum3
                
                colSum1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
                colSum2 = grid[row ][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
                colSum3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
                
                colEqual = colSum1 == colSum2 == colSum3

                
                diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
                diagonal2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
                
                diagonalEqual = diagonal1 == diagonal2
                
                if rowEqual == colEqual == diagonalEqual == True and len(uniqueBox) == len(allBox):
                    count += 1
        return count
                
                
                
                