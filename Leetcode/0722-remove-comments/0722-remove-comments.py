class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        #two states one to  read and one to ignore
        block = False
        newLine = False
        ans = []
        
        for line in source:
            
            i, temp, length = 0 , '', len(line)
            newLine = True if block else False
            
            while i <= length - 1:
                
                if not block and line[i] == '/' and i + 1 < length and line[i + 1] == '/':
                    break
                elif not block and line[i] == '/' and i + 1 < length and line[i + 1] == '*':
                    block = True
                    i = i + 2
                    continue 
                elif block and line[i] == '*' and i + 1 < length and line[i + 1] == '/':                
                    block = False
                    i = i + 2
                    continue
                elif block:
                    i += 1
                    continue
                temp += line[i]
                i += 1
            if newLine:
                ans[-1] += temp 
                newLine = False
            else:
                ans.append(temp)
        res = list(filter(lambda x : len(x) != 0, ans))
        return res
                    
                    
        