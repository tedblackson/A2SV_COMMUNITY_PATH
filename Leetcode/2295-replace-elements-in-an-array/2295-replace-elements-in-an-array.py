class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idxMapper = {}
                
        for i, num in enumerate(nums):
            idxMapper[num] = i
        
        for operation in operations:
            nums[idxMapper[operation[0]]]  = operation[1]
            idxMapper[operation[1]] = idxMapper[operation[0]]
            del idxMapper[operation[0]]
        
        return nums
                