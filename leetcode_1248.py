class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] %2 :
                nums[i] = 1
            else:
                nums[i] = 0
        
        
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
            
            
            
            
            
        
        
                