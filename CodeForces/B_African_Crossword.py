from collections import Counter, defaultdict
n, m  = map(int, input().split())

puzzle = []
row_count = {}
col_count = defaultdict(defaultdict)
for i in range(n):
    cur_row = list(input())
    row_count[i] = Counter(cur_row)
    puzzle.append(cur_row)

for i in range(m):
    temp = defaultdict(int)
    for j in range(n):
        temp[puzzle[j][i]] += 1
        col_count[i] = temp

ans = ''
for i in range(n):
    for j in range(m):
        if row_count[i][puzzle[i][j]] + col_count[j][puzzle[i][j]] == 2 :
                ans += puzzle[i][j]
        
print(ans)
    
    