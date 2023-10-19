class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        
        @cache
        def dp(idx, prev1, prev2):
            

            
            if idx == n:
                return 0
            
            ans = float(inf)
            
            valid = prev1 < nums1[idx] and prev2 < nums2[idx]
            validInverse = prev1 < nums2[idx] and prev2 < nums1[idx]
            
            if valid:
                ans =  min(ans, dp(idx + 1, nums1[idx], nums2[idx]))
                
            if validInverse:
                ans = min(ans, 1 + dp(idx + 1, nums2[idx], nums1[idx]))

        
            
            return ans
    
        return dp(0, -1, -1)
            
        