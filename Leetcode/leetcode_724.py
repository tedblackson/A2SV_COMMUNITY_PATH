class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans = 0
        prefix= [nums[0]]
        
        for i in range(1,len(nums)):
            prefix.append(prefix[i -1] +  nums[i])
        
        for i in range(len(nums)):
            if(prefix[i] - nums[i] == prefix[len(nums) -1] - prefix[i]):
                return i
        return -1