from math import ceil
N , D = map(int, input().split())

powers = list(map(int, input().split()))

powers.sort(reverse = True)

count = 0
n = 0
for power in powers:
    # print(n, power)
    if D%power == 0:
        temp = D/power + 1
    else:
        temp = ceil(D/power) 
    if n + temp  > N:
        break
    n += temp
    count += 1
print(count)
    

