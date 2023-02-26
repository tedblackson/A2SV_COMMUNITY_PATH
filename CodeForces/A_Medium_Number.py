N = int(input())

testCases = []

for _ in range(N):
    testCases.append(list(map(int, input().split())))
    
for testCase in testCases:
    testCase.sort()
    print(testCase[1])