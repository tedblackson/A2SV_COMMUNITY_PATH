class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        def predictor(left , right):
            
            if right == left:
                return nums[right]
            
            result1 = nums[left] - predictor(left + 1, right)
            result2 = nums[right] - predictor(left, right - 1)
            
            return max(result1, result2)
    
        ans = predictor(0, len(nums) -1)
        return ans >= 0