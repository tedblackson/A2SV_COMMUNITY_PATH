class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = right = total = 0
        ans = 0
        
        while right < len(arr):
            total += arr[right]
            while(right - left + 1 > k):
                total -= arr[left]
                left += 1
            if right - left + 1 == k and total/k >= threshold:
                ans += 1
            right += 1
        return ans