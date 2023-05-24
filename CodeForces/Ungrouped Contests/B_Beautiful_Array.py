N = int(input())

array = list(map(int, input().split()))

set1 = []
set2 = []
set3 = []

for num in array:
    if  num < 0:
        set1.append(num)
    elif num > 0:
        set2.append(num)
    else:
        set3.append(num)

if len(set1) % 2 == 0:
    set3.append(set1.pop())
if len(set2) == 0:
    set2.append(set1.pop())
    set2.append(set1.pop())

print(len(set1), *set1)
print(len(set2), *set2)
print(len(set3), *set3)

