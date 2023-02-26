class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for s in strs:
            if len(longest) > len(s):
                temp = ''
                for i, ch in enumerate(s):
                    if longest[i] == ch:
                        temp += ch
                    else:
                        break
                longest = temp
            else:
                temp = ''
                for i, ch in enumerate(longest):
                    if s[i] == ch:
                        temp += ch
                    else:
                        break
                longest = temp
        return longest
            

            

            
            
        

        
