H, W = map(int, input().split())

grid = []
for _ in range(H):
  grid.append(input())
 
directions = [ [1, 0] , [0, 1], [0, -1], [-1, 0], [-1, 1], [1, -1], [-1, -1], [1, 1]]

starts = []
def inBound (row, col):
    return 0 <= row < H and 0 <= col < W

for row in range(H):
    for col in range(W):
        if grid[row][col] == 's':
            starts.append((row, col))

for start in starts:
    
    for direction in directions:
        _row, _col = start
        temp = grid[_row][_col]
        
        path = [(start[0] + 1, start[1] + 1)]
        for _ in range(4):
            _row += direction[0]
            _col += direction[1]

            if inBound(_row, _col):
                temp += grid[_row][_col]
                path.append((_row + 1, _col + 1))
        
                
        if temp == "snuke":
            for ele in path:
                print(*ele)
            break
        
        