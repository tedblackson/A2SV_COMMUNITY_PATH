class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        right= currSum=ans= 0
    
        
        prefix = {}
    
        
        while(right < len(nums)):
            currSum += nums[right]
            if currSum == k:
                ans += 1
            if(prefix.get(currSum - k) != None):
                ans +=  prefix[currSum - k]
            
            if prefix.get(currSum) == None:
                prefix[currSum] = 1
            else:
                prefix[currSum] += 1
                
            right += 1
        return ans
            
            
            
