from collections import Counter
numTestCases = int(input())
testCases = []


for _ in range(numTestCases):
    testCases.append([list(map(int, input().split())), list(map(int, input().split()))])

for testCase in testCases:
    secCost = testCase[0][1]
    planets = testCase[1]
    cost = 0
    orbitCount = Counter(planets)
    
    planets.sort(key = lambda orbit : orbitCount[orbit], reverse = True)
    
    cost  = 0
    while planets:
        
        if secCost < orbitCount[planets[0]] :
            cost += secCost
            planets = planets[orbitCount[planets[0]]:]
        else:
            cost += orbitCount[planets[0]]
            planets = planets[orbitCount[planets[0]]:]
    print(cost)
        
        
        
        

