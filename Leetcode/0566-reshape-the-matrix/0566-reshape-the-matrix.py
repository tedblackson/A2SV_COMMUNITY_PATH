class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat) * len(mat[0])
        if r * c != n:
            return mat
        
        arr = []
        count = 0
        col = len(mat[0])
        temp = []


        for i in range(n):
            if count < c:
                temp.append(mat[i//col][i%col])
                count += 1
            else:
                arr.append(temp)
                temp = [mat[i//col][i%col]]
                count = 1
        arr.append(temp)
        return arr
            
        
        