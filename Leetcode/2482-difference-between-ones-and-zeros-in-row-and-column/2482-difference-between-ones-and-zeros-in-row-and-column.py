class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        cols = {}
        rows = {}
        diff = [ [0 for _ in grid[0]] for _ in grid]
        for row in range(len(grid)):
            zeros = 0
            for col in range(len(grid[0])):
                zeros = zeros + 1 if grid[row][col] == 0 else zeros
            rows[row] = zeros 
        for col in range(len(grid[0])):
            zeros = 0
            for row in range(len(grid)):
                zeros  = zeros + 1 if grid[row][col] == 0 else zeros
            cols[col] = zeros
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                diff[row][col] = len(grid[0]) - rows[row] + len(grid) - cols[col] - rows[row] - cols[col]
        return diff
                
            
                
        
        