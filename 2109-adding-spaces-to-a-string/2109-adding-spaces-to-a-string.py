class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        heapify(spaces)
        
        cur = heappop(spaces)
        newStr = ''
        for i, char in enumerate(s):
            
            if i == cur:
                newStr += ' ' + char
                cur = heappop(spaces) if spaces else cur
            else:
                newStr += char
        return newStr
            
        
        
        