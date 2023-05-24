N = int(input())
testCases = []

for _ in range(N):
    testCases.append([list(map(int, input().split())), list(map(int, input().split()))])
    


for testCase in testCases:
    min1 = min(testCase[0])
    min2 = min(testCase[1])
    
    max1 = max(testCase[0])
    max2 = max(testCase[1])
    
    if min1  + min2 == max1 == max2:
        print('Yes')
    else:
        print('No')
    
    
    

    

