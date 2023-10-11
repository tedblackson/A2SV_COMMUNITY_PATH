class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        
        @cache
        def dp(cur, group_one, group_two):
            
            if cur == n:
                return abs(group_one - group_two)
            
            res_one = dp(cur + 1, group_one + stones[cur], group_two)
            res_two = dp(cur + 1, group_one, group_two + stones[cur])
            
            return min(res_one, res_two)
        
        
        res = dp(0, 0, 0)
        
        return res