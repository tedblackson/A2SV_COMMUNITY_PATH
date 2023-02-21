class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        counted = Counter(words[0])
        ans = []
        
        for word in words[1:]:
            temp = Counter(word)
            for char in counted:
                if temp.get(char):
                    counted[char] = min(counted[char], temp[char])
                else:
                    counted[char] = 0
        for key, val in counted.items():
            while val > 0:
                ans.append(key)
                val -= 1
            
        return ans
        
        