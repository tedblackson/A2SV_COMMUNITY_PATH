N = int(input())

for _ in range(N):
    
    n = int(input())
    
    melody = input()
    cnt = 1
    i = 1
    start = melody[0] + melody[1]
    visited = set()
    visited.add(start)
    
    while i < n :
        temp = melody[i - 1]  + melody[i]
        
        if temp not in visited:
            visited.add(temp)  
            cnt += 1
                
        i += 1
    print(len(visited))
            