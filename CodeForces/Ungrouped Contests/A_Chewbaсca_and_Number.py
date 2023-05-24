number = list(input())

if 9 - int(number[0]) != 0:
    number[0] = str(min(int(number[0]), 9 - int(number[0])))
    
for i in range(1, len(number)):
    num = int(number[i])
    number[i] = str(min(num, 9 - num))
ans = ''.join(number)

print(ans)