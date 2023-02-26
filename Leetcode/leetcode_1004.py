class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = ans = 0
        
        while(right < len(nums)):
            
            
            while k < 0:
                if nums[left] == 0:
                    k +=1
                left += 1

            if nums[right] == 0:
                k -= 1
            if nums[right] == 0 and k < 0:    
                ans = max(right - left , ans)
            else: 
                ans = max(right - left + 1, ans)
                
            
            right += 1
            
        return ans