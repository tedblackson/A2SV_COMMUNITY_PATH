nums = list(map(int , input().split()))

results = list(map(int, input().split()))

promoted = 0

for result in results:
    if result > nums[1]:
        promoted += 1
print(promoted)