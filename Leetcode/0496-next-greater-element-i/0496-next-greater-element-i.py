class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {}
        stack = []
        
        for val in nums2:
            while stack and stack[-1] < val:
                mapp[stack.pop()] = val
            stack.append(val)
        ans = list(map(lambda ele : mapp.get(ele) if mapp.get(ele) else -1, nums1))
        return ans