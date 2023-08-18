class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = [(val + nums2[0], i, 0)   for i, val in enumerate(nums1)]
        
        ans = []
        
        while heap and k > 0:
            
            cur, idx1, idx2 = heappop(heap)
            
            ans.append([nums1[idx1], nums2[idx2]])
            idx2 += 1
            if idx2 < len(nums2):
                temp = (nums1[idx1] + nums2[idx2], idx1, idx2)
                heappush(heap, temp)
            k -= 1
            
        
        return ans
        