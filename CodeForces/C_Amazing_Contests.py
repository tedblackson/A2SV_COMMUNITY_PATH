numContests = int(input())

contests = list(map(int, input().split()))

minimum = maximum = contests[0]

count = 0
for point in contests[1:]:
    if point < minimum:
        count += 1
        minimum = point
    elif point > maximum:
        count += 1
        maximum = point
print(count)