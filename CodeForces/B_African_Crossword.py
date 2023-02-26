from collections import Counter
size = map(int , input().split())

rowSize = size[0]

crossPuzzle = []
for _ in range(rowSize):
    crossPuzzle.append(input())

rowRepeated = {}
columnRepeated = {}

for row in crossPuzzle:
    counted = Counter(row)
    
    repeated = set(filter(lambda key : counted[key] >= 2 , counted.keys()))
    

for col in range(len(crossPuzzle[0])):
    counted = {}
    
    for row in range(len(crossPuzzle)):
        cur = crossPuzzle[row][col]
        if counted.get(cur):
            counted[cur] += 1
        else:
            counted[cur] = 1
    repeated = set(filter(lambda key : counted[key] > 1, counted.keys()))
        
    