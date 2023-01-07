class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0]  * len(nums)
        i = 0
        k = 1
        for num in nums:
            if i < len(nums) and num > 0:
                ans[i] = num
                i += 2
            else:
                ans[k] = num
                k += 2
                    
        return ans
                