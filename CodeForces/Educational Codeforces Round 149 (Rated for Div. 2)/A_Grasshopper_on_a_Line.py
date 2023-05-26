N = int(input())

for _ in range(N):
    x, k = map(int, input().split())
    
    if x %k:
        print(1)
        print(x)
    else:
        for i in range(-100, 101):
            flag = False
            for j in range(-100, 101):
                if i != j and i %k and j %k :
                    if i + j == x:
                        print(2)
                        print(i, j)
                        flag = True
                        break
            if flag:
                break
            
            
            
            
            
            
        
    
    
        