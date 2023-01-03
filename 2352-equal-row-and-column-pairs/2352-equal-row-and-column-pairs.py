class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rowCount = defaultdict(int)
        colCount = defaultdict(int)
        ans = 0
        
        for col in range(len(grid[0])):
            temp = []
            for row in range(len(grid)):
                temp.append(grid[row][col])
            rowCount[tuple(temp)] += 1
        
        for row in range(len(grid)):
            temp = []
            
            for col in range(len(grid[0])):
                temp.append(grid[row][col])
            colCount[tuple(temp)] += 1
        
        for key, value in rowCount.items():
            ans += value * (colCount[key])
        return ans
            
        
                
        