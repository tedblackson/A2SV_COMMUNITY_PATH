class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = ans = 0
        k = 1
        temp = []
        while right < len(nums):
            
            if nums[right] == 0:
                    k -= 1
            while k < 0:
                if nums[left] == 0:
                    k +=1
                left +=1
            
            ans = max(ans , right - left)  
            right +=1
        return ans
                
                
            