N = int(input())
testCases = []

for _ in range(N):
    board = []
    for _ in range(8):
        board.append(input())
    print(board)
    testCases.append(board)


# for testCase in testCases:
    
#     board = testCase
    
#     for row in range(1, 7):
#         attacked = board[row].count('#')
        
#         for col in range(1, 7):
#             if board[row][col] == "#" and attacked == 1:
                

#                 if board[row + 1][col + 1] == board[row + 1][col - 1] == "#":
#                     print(row + 1, col + 1)
    

