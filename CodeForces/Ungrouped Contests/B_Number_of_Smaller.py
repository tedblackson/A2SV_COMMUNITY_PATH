m , n = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

two = count = 0

for i in range(m):
    while second[two] < first[i]:
        second[two] = i + 1
        
print(*second)
        
