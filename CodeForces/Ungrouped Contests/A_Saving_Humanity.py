N = int(input())
            
for _ in range(N):
    
    n , m = map(int, input().split())
            
    initial = input()
    initial = '0' + initial + '0'
    state = list(initial)
    prev, cur = '', initial
    
    for k in range(m):
        if prev == cur:
            break
        
        for i in range(1, n + 1):
            if initial[i] == '0':
                if int(initial[i -1]) + int(initial[i + 1])  == 1:
                    state[i] = '1'
                    
        prev = initial
        initial = ''.join(state)
        cur = initial
        
    print(initial[1:n + 1])
                