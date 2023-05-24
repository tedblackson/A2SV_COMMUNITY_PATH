N, M = map(int, input().split())
grid = []


for _ in range(N):
    grid.append(input())
    
visited = set()
def valid(first, second):
    cnt = 0
    for i in range(M):
        if first[i] != second[i]:
            cnt += 1
    return cnt <= 1
            
def backtrack(cur):
    
    if len(visited) == N: 
        return True
    
    for ele in grid:
        if ele not in visited:
            if valid(ele, cur):
                visited.add(ele)
                if backtrack(ele):
                    return True
                visited.remove(ele)
        
        
    
    
for i in range(N):
    if backtrack(grid[i]):
        print("Yes")
        exit()
    
print("No")
    
            