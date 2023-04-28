class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        level = 1
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1] , [1, 1], [-1, -1], [1, -1], [-1, 1] ]
        visited , queue = set(), deque()
        queue.append((0, 0))
        visited.add((0,0))
        n = len(grid)
        
        if grid[0][0] == 1:
            return -1
        
        def inBound(row, col):
            return 0 <= row <  n and 0 <= col < n
        temp = []
        while queue:
            src = queue.popleft()
            if src == (n -1, n -1):
                return level
            for direction in directions:
                _row = src[0] + direction[0]
                _col = src[1] + direction[1]
                
                if inBound(_row, _col) and not grid[_row][_col] and (_row, _col) not in visited:
                    visited.add((_row, _col))
                    temp.append((_row, _col))
            if not queue and temp:
                queue = deque(temp)
                level += 1
                temp = []
        return -1
            
                    
                    
        
        