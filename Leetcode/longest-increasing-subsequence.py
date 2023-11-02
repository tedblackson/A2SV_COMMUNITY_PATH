class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
          _max = 0
          for j in range(i):
            if nums[j] < nums[i]:
              _max = max(_max, dp[j])
          dp[i] += _max

        return max(dp)
