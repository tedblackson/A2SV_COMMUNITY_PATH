N = int(input())

for _ in range(N):
    left, right = map(int, input().split())
    
  
    for i in range(left, right + 1):
        done =False
        for j in range(left , right + 1):
            
            if i % j == 0 and i != j:
                print(i, j)
                done = True
                break
        if done:
            break
        
                