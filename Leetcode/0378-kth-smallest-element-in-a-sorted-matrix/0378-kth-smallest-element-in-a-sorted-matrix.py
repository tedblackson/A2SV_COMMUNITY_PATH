class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        for i in range(1, len(matrix)):
            matrix[0] += matrix[i]
        heapify(matrix[0])
        
        while k > 1:
            heappop(matrix[0])
            k -= 1
        ans = heappop(matrix[0])
        return ans
            
            