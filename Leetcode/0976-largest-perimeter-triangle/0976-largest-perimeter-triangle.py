class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(len(nums) -1, 1, -1):
            
            total = nums[i] + nums[i - 1] + nums[i -2]

            if nums[i] + nums[i - 1] > nums[i -2] and nums[i -1] + nums[i -2] > nums[i] and nums[i] + nums[i -2] > nums[i -1]:
                ans = max(ans, total)
        return ans



        