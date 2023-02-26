from collections import Counter
numTestCase  = int(input())

testCases = []

for _ in range(numTestCase):
    testCases.append([int(input()), list(map(int, input().split())), input()])
    

for testCase in testCases:
    mapper = {}
    for char, num in zip(testCase[2], testCase[1]):
        mapper[num] = char
    for i in range(len(testCase[1])):
        testCase[1][i] = mapper[testCase[1][i]]
    if ''.join(testCase[1]) == testCase[2]:
        print('YES')
    else:
        print("NO")
        
        
    

    

    
        
            
            
    
    