from collections import Counter
numTestCase = int(input())

testCases = []

for _ in range(numTestCase):
    testCases.append(input().split())

for testCase in testCases:
    count1 = Counter(testCase[0])
    count2 = Counter(testCase[1])
    mapper = {'S': -1, 'M' : 2, 'L' : 3, 'X' : 4}
    
    val1 = val2 = 1
    for key , val in count1.items():
        val1 *= (val * mapper[key])
    for key, val in count2.items():
        val2 *= (val * mapper[key])
    if val1 < val2:
        print('<')
    elif val1 > val2:
        print('>')
    else:
        print('=')
    
    
          