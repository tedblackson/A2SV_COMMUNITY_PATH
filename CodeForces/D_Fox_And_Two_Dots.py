from collections import defaultdict
import sys, threading

def main():
    n, m = map(int, input().split())
    directions = [[-1,  0], [1, 0], [0, 1], [0, -1]]
    colors = defaultdict(int)
    board = []
    for _ in range(n):
        board.append(input())

    def inBound(row, col):
        return 0 <= row < n and 0 <= col < m

    def dfs(row, col, parent):
        if colors[(row, col)] == 1:
            return True

        colors[(row, col)] = 1

        for direction in directions:
            _row = direction[0] + row
            _col = direction[1] + col

            if inBound(_row, _col ) and board[_row][_col] == board[row][col] and (_row, _col) != parent:
                if colors[(_row, _col)] == 0:
                    if dfs(_row, _col, (row, col)):
                        return True
                elif colors[(_row, _col)] == 1:
                    return True



        colors[(row, col)] = 2
        return False

    for row in range(n):
        for col in range(m):
            if colors[(row, col)] == 0:
                if dfs(row, col, None):
                    print("Yes")
                    exit()
    print("No")

sys.setrecursionlimit(10**9)
threading.stack_size(1 << 27)
mainthread = threading.Thread(target=main)
mainthread.start()
mainthread.join()