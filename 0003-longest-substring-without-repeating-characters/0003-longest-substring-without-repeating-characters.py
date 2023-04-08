class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = 0
        visited = set()

        for end in range(len(s)):
            
            while s[end] in visited:
                visited.remove(s[start])
                start += 1
            visited.add(s[end])
            ans = max(end - start + 1, ans)
            
        return ans
            
            
            
            