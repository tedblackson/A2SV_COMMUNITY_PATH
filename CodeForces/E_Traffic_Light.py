n = int(input())
testCases = []

for _ in range(n):
    testCases.append([input().split(), input()])


for testCase in testCases:
    newString = testCase[1] * 2
    green = False
    guarranted  = 0
    
    for i in range(len(newString) -1 , -1, -1):
        if newString[i] == 'g':
            green = i
        elif green and newString[i] == testCase[0][1] :
            guarranted = max(guarranted, green - i)
    print(guarranted)
            
            
            
        
        
        
            
    
    
        
            
    
    
    
    
    
    

    
    


    
