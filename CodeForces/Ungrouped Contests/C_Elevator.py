N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    
    optimal = min(nums[0] * 4, nums[1]*4 + nums[1] * nums[2], nums[0] * nums[2] + nums[1] * (4 - nums[2]))
    print(optimal)