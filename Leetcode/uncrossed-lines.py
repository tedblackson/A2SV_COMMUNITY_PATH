class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        
        @cache
        def dp(i, j):
            
            if i == n or j == m:
                return 0
            ans = 0
            if nums1[i] == nums2[j]:
                ans += 1 + dp(i + 1, j + 1)
            else:
                ans = max( dp(i + 1, j), dp(i, j + 1), ans)
            
            return ans
            
        ans = dp(0, 0)
        return ans
            
            