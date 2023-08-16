class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        target = [[1, 2, 3], [4, 5, 0]]
        

        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        loc = None
        
        def inBound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    loc = (row, col)
        
        queue = deque(((copy.deepcopy(board), loc),))
        level = 0
        
        visited = set()
        
        while queue:
            
            for _ in range(len(queue)):
                
                src, loc = queue.popleft()
                
                if src == target:
                    return level
                
                for direction in directions:
                    temp = copy.deepcopy(src)
                    row, col = loc
                    _row = row + direction[0]
                    _col = col + direction[1]
                    
                    
                    if inBound(_row, _col) :
                        temp[row][col], temp[_row][_col] = temp[_row][_col], temp[row][col]
                        tup = tuple( tuple(row) for row in temp)
                        if tup not in visited:
                            visited.add(tup)
                            queue.append((copy.deepcopy(temp), (_row, _col)))
            level += 1
        return -1
                        
            
            
                
                
        
        