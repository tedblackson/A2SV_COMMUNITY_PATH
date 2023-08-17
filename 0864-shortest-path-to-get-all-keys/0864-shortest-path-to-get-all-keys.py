class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
    
        target = cur = 0
        visited = set()
        start = None
        level = 0
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if 97 <= ord(grid[row][col]) <= 122:
                    target = target | (1 << (ord(grid[row][col]) - 97))
                elif grid[row][col] == "@":
                    start = (row, col)
        
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col  < len(grid[0])
        
        queue = deque([[start, cur]])
        visited.add((start, cur))
        
        while queue:
            
        
            for i in range(len(queue)):
                
                (row, col), cur =  queue.popleft()
                
                if cur == target:
                    return level
                

                for direction in directions:
                    tempCur = cur
                    _row = row + direction[0]
                    _col = col + direction[1]
                    
                    if inBound(_row, _col) and ((_row, _col), tempCur) not in visited:
                        visited.add(((_row, _col), cur))
                        if grid[_row][_col] == "." or grid[_row][_col] == "@":
                            queue.append(((_row, _col), tempCur))
                        elif grid[_row][_col].islower():
                            tempCur = tempCur | (1 << (ord(grid[_row][_col]) - 97))
                            queue.append(((_row, _col), tempCur))
                            visited.add(((_row, _col), tempCur))
                        elif grid[_row][_col].isupper() and tempCur & (1 << (ord(grid[_row][_col].lower()) - 97)):
                            queue.append(((_row, _col), tempCur))
   

            level += 1
            
        
        
                    
    
            
            
        return -1
                    