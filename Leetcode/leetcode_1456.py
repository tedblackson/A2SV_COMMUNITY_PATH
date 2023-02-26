class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e', 'i', 'o', 'u'}
        
        left = right = ans= res = 0
        temp = []
        
        while right <  len(s):
            
            if(len(temp) <= k):
                temp.append(s[right])
                if s[right] in vowels:
                    ans += 1
                right += 1
            if len(temp) > k:
                if s[left] in vowels:
                    ans -= 1  
                temp.pop(0)
                left += 1
            res = max(res, ans)
        return res