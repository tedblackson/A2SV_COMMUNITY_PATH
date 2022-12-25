# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
size = list(map(int, input().split()))
groupB = []

groupA = defaultdict(list)

for i in range(1, size[0] + 1):
    groupA[input()].append(i)

for _ in range(size[1]):
    groupB.append(input())
for ele in groupB:
    if groupA[ele]:
        print(*groupA[ele])
    else:
        print(-1)


