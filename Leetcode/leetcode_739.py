class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        tempStack = []
        
        for i in range(len(temperatures)):
        
            while(len(tempStack) > 0 and temperatures[tempStack[-1]] < temperatures[i]):
                current = tempStack.pop()
                
                result[current] = i  - current
                
            tempStack.append(i)
        
        return result