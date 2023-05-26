N = int(input())

for _ in range(N):
    
    s = input()
    ans = ''
    zero = True
    
    for chr in s:
        if chr == "?" and zero:
            ans += "0"
        elif chr == "?" and not zero:
            ans += "1"
        
        elif chr == "0":
            ans += chr
            zero = True
        elif chr == "1":
            ans += chr
            zero = False
    print(ans)