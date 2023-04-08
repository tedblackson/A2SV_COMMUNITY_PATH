n = int(input())
planes = list(map(int, input().split()))

ans = []
for i in range(n):
    one = planes[i]
    two = planes[one -1]
    three = planes[two -1]
    if i + 1 == three:
        print('YES')
        break
else:
    print('NO')
    

    