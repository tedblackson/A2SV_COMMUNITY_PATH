# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())
testcases = []

for i in range(n):
    testcases.append([input(), input().split(" ")])

for testcase in testcases:
    left = 0
    right = int(testcase[0]) - 1
    top = math.inf
    ans = ''
    while left <= right:
        if top >= int(testcase[1][right]) >= int(testcase[1][left]):
            top  = int(testcase[1][right])
            right -= 1
        elif top >= int(testcase[1][left]) >= int(testcase[1][right]):
            top = int(testcase[1][left])
            left += 1
        else:
            ans = 'No'
            break
    
    ans = 'Yes' if not ans else ans
    print(ans)
            
            
    
            
            
        
    
