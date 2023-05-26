N = int(input())

for _ in range(N):
    n = int(input())
    start = 0
    unique = {0}
    s = input()
    prev = None
    _max = 1
    cnt = 1

    for i in range(1, n):
        
        if s[i] == s[i - 1]:
            cnt += 1
            _max = max(cnt, _max) 
              
        else:
            cnt = 1

        
    print(_max + 1)