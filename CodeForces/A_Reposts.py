from collections import defaultdict

n = int(input())

tree = defaultdict(list)
for _ in range(n):
    
    child, _ , parent = input().split()
    tree[parent.lower()].append(child.lower())

stack = ['polycarp']
ans = [0]
def maxdepth(root, depth = 1):
    
    if not tree[root]:
        ans[0] = max(ans[0], depth)
        return
    for child in tree[root]:
        maxdepth(child, depth + 1)
        
maxdepth('polycarp',1)

print(ans[0])