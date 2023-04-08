class Solution:
    def maxProduct(self, words: List[str]) -> int:
        offset = 97
        _binary = []
        
        for word in words:
            mask = 0
            for ele in word:
                mask |= 1 << (ord(ele) - offset)
            _binary.append(mask)
            
        def check(first, second):
            while first and second:
                if first & 1 and second & 1 :
                    return False
                first >>= 1
                second >>= 1
            
            return True
        ans = 0
        for i in range(len(_binary)):
            first = _binary[i]
            for j in range(i + 1, len(_binary)):
                second = _binary[j]
                if check(first, second):
                
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans