N = int(input())

for _ in range(N):
    string = input()
    res = ''
    right = len(string) - 1
    left = len(string) - 2
    
    while right > 0:
        if string[right] != string[right- 1]:
            res += string[right]
            right -= 1
        else:
            right -= 2
            
    print(res) 