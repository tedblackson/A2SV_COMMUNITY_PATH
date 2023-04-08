t = int(input())

for _ in range(t):
    row, col = map(int, input().split())
    directions = [[-1, -1], [1,1], [-1, 1], [1, -1]]
    
    chessboard = []
    
    for _ in range(row):
        chessboard.append(list(map(int, input().split())))
    ans = 0
    
    for i in range(row):
        for j in range(col):
            total = chessboard[i][j]
            
            for direction in directions:
                temp = [i, j]

                while -1 < direction[0] + temp[0] < row and -1 < direction[1] + temp[1] < col:
                    temp[0] += direction[0]
                    temp[1] += direction[1]
                    total += chessboard[temp[0]][temp[1]]
            ans = max(ans, total)
    print(ans)
                
                    
                    