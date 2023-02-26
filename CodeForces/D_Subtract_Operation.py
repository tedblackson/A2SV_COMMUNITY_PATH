N = int(input())

for _ in range(N):
    
    n, target = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    numbers.sort()
    total = sum(numbers)
    
    mult = n
    subt = 0
    for  i, num in enumerate(numbers[:n - 1]):
        if i == n - 2:
            total -= (num - subt)
        else:
            total -= (mult * (num - subt))
            subt += (num  - subt)
        mult -= 1
    if total == target:
        print('YES')
    else:
        print('NO')
        
        