N = int(input())
 
laptops = []
 
for _ in range(N):
    laptops.append(tuple(map(int, input().split())))
 
laptops.sort()
 
for i in range(len(laptops) - 1):
    if laptops[i][1] > laptops[i + 1][1]:
        print('Happy Alex')
        exit()

print('Poor Alex')