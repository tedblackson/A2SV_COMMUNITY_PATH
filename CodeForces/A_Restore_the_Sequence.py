N = int(input())

for _ in range(N):
    
    n = int(input())
    sequence = list(map(int, input().split()))
    
    left = 0
    right = n - 1
    turn = 0
    while left <= right:
        
        if turn%2:
            print(sequence[right], end = ' ')
            right -= 1
        else:
            print(sequence[left], end = ' ')
            left +=1 
        turn += 1
    print()
    