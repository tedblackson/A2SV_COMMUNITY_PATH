class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less = len(list(filter(lambda x : x <= pivot, nums)))
        ans = [0] * len(nums)
        
        left = 0
        equal = less - 1
        right = less
        
        for num in nums:
            if num < pivot:
                ans[left] = num
                left += 1
            elif num > pivot:
                ans[right] = num
                right += 1
            else:
                ans[equal] = num
                equal -= 1
        return ans
                
        
        