n , a , b = map(int, input().split())
from collections import defaultdict

problems = list(map(int, input().split()))

def count(bound):
    curSum  = 0
    start = 0
    ans= 0
    for end in range(n):
        curSum += problems[end]
        while curSum  > bound:
            curSum -= problems[start]
            start += 1    

        ans += end - start +1
    return ans

ans = count(b) - count(a -1)
print(ans)

        
    
    
    
    
    