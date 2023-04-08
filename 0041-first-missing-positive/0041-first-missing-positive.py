class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = []
        
        for ele in nums:
            if ele > 0:
                arr.append(ele)
        
        start = 0
        
        arr.sort()
        for ele in arr:
            if ele == start + 1:
                start += 1
            elif ele == start:
                continue
            else:
                return start + 1
        return start + 1
                
