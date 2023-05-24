class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[-1, 0],[1, 0], [0, -1], [0, 1]]
        visited = set()
        
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            
            visited.add((row,col))
            if grid[row][col] == 1:
                area[0] += 1
            
            if grid[row][col] == 0:
                return
            for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if inBound(new_row, new_col) and (new_row, new_col) not in visited:
                        dfs(new_row, new_col)
                    
        ans = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                area = [0]
                if (row, col) not in visited:
                    dfs(row, col)
                ans = max(area[0], ans)
        return ans
                    
        
            
            
        
        
                
                
        