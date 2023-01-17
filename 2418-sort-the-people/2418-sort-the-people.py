class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        for i in range(len(heights)):
            smallest = -math.inf
            index = 0
            for j in range(i , len(heights)):
                if heights[j] > smallest:
                    smallest = heights[j]
                    index = j
            heights[i], heights[index] = heights[index], heights[i]
            names[i], names[index] = names[index], names[i]
            
        return names
                
        
        