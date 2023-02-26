N = int(input())

testCases = []

for _ in range(N):
    
    testCases.append([list(map(int, input().split())), list(map(int, input().split()))])
    

for testCase in testCases:
    count = 0
    print(testCase[0])
    
    for i in range(testCase[0][0] - testCase[0][1]):
        if testCase[1][i] * pow(2, i) < testCase[1][i + 1] * pow(2, i + 1):
            count += 1
    print(count)
        