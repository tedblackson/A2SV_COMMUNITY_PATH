from collections import defaultdict
n = int(input())
tree = defaultdict(list)

def lower(word):
    word = word.lower()
    return word
for _ in range(n):
    child, _ , parent = map(lower, input().split())
    tree[parent].append(child)
# print(tree)

ans = [0]
def dfs(root, depth):
    ans[0] = max(ans[0], depth)
    

    for child in tree[root]:
        dfs(child, depth + 1)
        
dfs("polycarp", 1)
print(ans[0])
    
    
    
    
    
    