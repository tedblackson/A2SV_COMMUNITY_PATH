class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ans = []

        for ele_one in firstList:
            for ele_two in secondList:
                temp = [ele_one, ele_two]
                temp.sort()

                if temp[1][0] <= temp[0][1]:
                    ans.append([temp[1][0], min(temp[0][1], temp[1][1])])
        return ans

        