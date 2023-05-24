from collections import defaultdict, Counter

q = int(input())

for _ in range(q):
    n = int(input())
    sides = list(map(int, input().split()))
    sides.sort()
    ans = set()
    left = 0
    right = 4 * n - 1
    
    while left < right:
        if sides[left] != sides[left+1] or sides[right] != sides[right-1] or sides[left] * sides[right] != sides[left+2] * sides[right-2]:
            print("NO")
            break
        ans.add(sides[left] * sides[right])
        left += 2
        right -= 2
    else:
        if len(ans) == 1:
            print("YES")
        else:
            print("NO")
