class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [1, 0], [-1, 0], [0, -1]]
        m , n = len(grid) , len(grid[0])
        
        def bfs(start):
            
            queue = deque([start])
            level = 0
            
            while queue:
                
                for _ in range(len(queue)):
                    
                    row, col = queue.popleft()
                    if grid[row][col] == 2:
                        return level - 1
                    for direction in directions:
                        _row = row + direction[0]
                        _col = col + direction[1]
                        
                        if inBound(_row, _col) and grid[_row][_col] != 1 and (_row, _col) not in visited:
                            visited.add((_row, _col))
                            queue.append((_row, _col))
                
                level +=1 
                
        
        def dfs(row, col):
            
            for direction in directions:
                _row    = direction[0] + row
                _col = direction[1] + col
                
                if inBound(_row, _col) and grid[_row][_col] == 1 :
                    grid[_row][_col] += 1
                    dfs(_row, _col)
        
        
        def inBound(row, col):
            return 0 <= row < m  and 0 <= col < n
        
        start = None
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    start = (row, col)
        grid[start[0]][start[1]] +=1 
        dfs(*start)
        
        ans = math.inf
        for row in range(m):
            for col in range(m):
                if grid[row][col] == 1:
                    visited = set()
                    temp = bfs((row, col))
                    ans = min(ans, temp if temp != None else math.inf)
        
        return ans
        
        
                