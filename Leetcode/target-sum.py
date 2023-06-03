class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        
        
        @cache
        def countWays(cur_sum, cur):
         
            if cur_sum == 0 and cur == n :
                return 1
            if cur >= n:
                return 0
            
            cnt = 0
            
            cnt += countWays(cur_sum - nums[cur], cur + 1)
            cnt += countWays(cur_sum + nums[cur], cur + 1)
            
            
            return cnt
        
        
        return countWays(target, 0)
            