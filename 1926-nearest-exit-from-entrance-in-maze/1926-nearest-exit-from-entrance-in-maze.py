class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        queue , visited = deque(), set()
        queue.append(entrance)
        visited.add(entrance)
        temp, level = [], 0
        _rows , _cols =  len(maze), len(maze[0]),
    
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def inBound(row, col):
            return 0 <= row < _rows and 0 <= col < _cols
        
        while queue:
            
            src = queue.popleft()
            cond1 = src[0] * src[1] == 0
            cond2 = (src[0] == _rows -1) or (src[1] == _cols - 1)
            
            if src != entrance and (cond1 or cond2):
                
                return level
                
            
            for direction in directions:
                row = direction[0] + src[0]
                col = direction[1] + src[1]
                
                if inBound(row, col) and (row, col ) not in visited and maze[row][col] == '.':
                    temp.append((row, col))
                    visited.add((row, col))
                
            if not queue and temp:
                queue = deque(temp)
                temp = []
                level += 1
        return -1
                    
            
            
            
            
        
        