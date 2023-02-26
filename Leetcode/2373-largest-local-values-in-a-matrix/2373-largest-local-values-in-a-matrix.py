class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        maxLocal = [[0]* (len(grid) - 2) for _ in range(len(grid) - 2)]
        
        
        for row in range(0, len(grid) - 2):
            for col in range(0, len(grid) - 2):
                maxx = 0
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        maxx = max(maxx, grid[i][j])
                maxLocal[row][col] = maxx
        return maxLocal