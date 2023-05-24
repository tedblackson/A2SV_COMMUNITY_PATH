from functools import lru_cache
import threading
from sys import stdin,stdout,setrecursionlimit
from collections import defaultdict

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def inp():
    return stdin.readline()
def inpnum():
    return int(stdin.readline())
def inpli():
    return list(map(int, stdin.readline().strip().split()))
def inpst():
    s = stdin.readline().strip()
    return list(s[:len(s)])
def inpnums():
    return map(int, stdin.readline().strip().split())

def main():

    graph = defaultdict(list)

    for _ in range(inpnum()):
        src, dest  = inpli()

        graph[src].append(dest)
        graph[dest].append(src)



    visited = set()
    ans = []
    def dfs(root):
        ans.append(root)
        for child in graph[root]:
            if child not in visited:
                visited.add(child)
                dfs(child)

    for key, val in graph.items():
        if len(val)  == 1:
            visited.add(key)
            dfs(key)
            print(*ans)
            exit()

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()