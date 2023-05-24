
from functools import lru_cache
import threading
from sys import stdin,stdout,setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def inp():return stdin.readline()
def inpnum():return int(stdin.readline())
def inpli():return list(map(int, stdin.readline().strip().split()))
def inpst():
    s = stdin.readline().strip()
    return list(s[:len(s)])
def inpnums():return map(int, stdin.readline().strip().split())

def main():
    N = inpnum()
    directions = [[-1, 0], [1, 0], [0,1], [0, -1]]
    def dfs(root):
        stack =[root]
        
        while stack:
            row, col = stack.pop()
            
            volume[0] += lakes[row][col]
            ans[0] = max(ans[0], volume[0])
            for direction in directions:
                _row = row + direction[0]
                _col = col + direction[1]
                
                if inBound(_row, _col) and lakes[_row][_col] > 0 and  (_row, _col) not in visited:
                    visited.add((_row, _col))
                    stack.append((_row, _col))


    for _ in range(N):
        visited = set()
        ans = [0]
        lakes = []
        n, m  = inpli()
        
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m

        for _ in range(n):
            lakes.append(inpli())

        for row in range(n):
            for col in range(m):
                if lakes[row][col] > 0 and (row, col) not in visited:
                    volume = [0]
                    visited.add((row, col))
                    dfs((row, col))

        print(ans[0])
    
    
    

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()