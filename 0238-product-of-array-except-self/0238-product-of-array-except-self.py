class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)
        product1 = product2 = 1
        
        for i in range(len(nums)):
            answer[i] = product1
            product1 *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            answer[j] *= product2
            product2 *= nums[j]
                
        return answer