numTestcases = int(input())

testCases = []

for _ in range(numTestcases):
    testCases.append(input().split())

for testCase in testCases:
    def fun(word):
        for char in word:
            if char.isnumeric():
                return int(char)
    testCase.sort(key = fun)
    
    for i, word in enumerate(testCase):
        for letter in word:
            if not letter.isnumeric():
                print(letter, end = '')
        if i != len(testCase) - 1:
            print(end = ' ')
    print()
    
    
    