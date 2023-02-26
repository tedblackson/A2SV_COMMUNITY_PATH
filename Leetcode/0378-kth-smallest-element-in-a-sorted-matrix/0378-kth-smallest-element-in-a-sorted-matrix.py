class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = 0
        flatMatrix  = sum(matrix, [])
        heapify(flatMatrix)
        for i in range(k):
            ans = heappop(flatMatrix)
        return ans
            
        