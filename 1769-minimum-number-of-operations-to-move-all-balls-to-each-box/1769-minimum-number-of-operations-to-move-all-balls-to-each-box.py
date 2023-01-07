class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        
        for i, box1 in enumerate(boxes):
            temp = 0
            for j, box2 in enumerate(boxes):
                if i != j and boxes[j] == '1':
                    temp += abs(i - j)
            ans.append(temp)
        return ans
        