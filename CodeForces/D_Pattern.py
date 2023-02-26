numPatterns = int(input())

patterns = []

for _ in range(numPatterns):
    patterns.append(list(input()))
    
ans = ['?'] * len(patterns[0])
for i in range(len(patterns[0])):
    temp = '?'
    change = True
    for j in range(len(patterns)):
        if temp == '?'  :
            ans[i] = patterns[j][i]
            temp = patterns[j][i]
        elif patterns[j][i] == temp:
            ans[i] = temp
        elif patterns[j][i] != '?':
            ans[i] = '?'
            change = False
    if change and ans[i] == '?':
         ans[i] = 'c'         
print(''.join(ans))
    
            
            