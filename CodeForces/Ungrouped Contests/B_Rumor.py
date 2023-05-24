

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
    from collections import defaultdict

    n , m = map(int, input().split())
    golds = list(map(int, input().split()))
    graph = defaultdict(list)
    spreaders = list(range(1, n + 1))
    spreaders.sort(key = lambda ele: golds[ele -1])
    for _ in range(m):
        src, dest = map(int, input().split())
        graph[src].append(dest)
        graph[dest].append(src)


    visited = set()
    def dfs(root):

        for child in graph[root]:
            if child not in visited:
                visited.add(child)
                dfs(child)

    ans = 0
    for ele in spreaders:
        if ele not in visited:
            ans += golds[ele - 1]
            visited.add(ele)
            dfs(ele)
    print(ans)
    
    

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()