N= int(input())

for _ in range(N):
    n = int(input())
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    grid = []
    for _ in range(2):
        grid.append(input())
        
    def inBound(row, col):
        return 0 <= row < 2 and 0 <= col < n

    visited = set()
    flag = [False]
    def dfs(root):
        if root[0] ==1 and root[1] == n - 1:
            flag[0] = True
            return
        for direction in directions:
            _row = direction[0] + root[0]
            _col = direction[1] + root[1]
        
            
            if inBound(_row, _col) and grid[_row][_col] == "0" and (_row, _col) not in visited:
                visited.add((_row, _col))
                dfs((_row, _col))
    dfs((0, 0))
    print("YES") if flag[0] else print("NO")
    
                
        
    
    