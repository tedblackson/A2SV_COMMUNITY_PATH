class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        def predictor(left , right):
            
            if right - left + 1 == 1:
                return [nums[right], 0]
            
            
            pred_l = predictor(left + 1, right)
            pred_r = predictor(left, right - 1)
            
            result = [nums[left] + pred_l[1], nums[right] + pred_r[1]]
            
            if result[0] > result[1]:
                p1 = result[0]
                p2 = pred_l[0]
            elif result[0] < result[1]:
                p1 = result[1]
                p2 = pred_r[0]
            else:
                p1 = result[0]
                p2 = min(pred_l[0], pred_r[0])
                
            return p1, p2
        
        
        result = predictor(0, len(nums) - 1)
        return result[0] >= result[1]