class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = right = 0
        ans = []
        vals =  dict(Counter(p))
        temp = []
        sub = {}
        while right < len(s):
            if len(temp) <= len(p):
                temp.append(s[right])
                if sub.get(s[right]) == None:
                    sub[s[right]] = 1
                else:
                    sub[s[right]] += 1
                right  += 1
            if len(temp) > len(p):
                temp.pop(0)
                sub[s[left]]-=1
                if(sub[s[left]] == 0):
                    del sub[s[left]]
                left += 1
            if vals == sub:
                ans.append(left)
        return ans    