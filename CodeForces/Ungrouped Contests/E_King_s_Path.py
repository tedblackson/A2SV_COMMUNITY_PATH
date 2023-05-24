from collections import defaultdict
x1, y1, x2, y2 = map(int, input().split())

allowed = defaultdict(list)
n = int(input())

for _ in range(n):
    temp = list(map(int, input().split()))
    allowed[temp[0]] =temp[1:]


    