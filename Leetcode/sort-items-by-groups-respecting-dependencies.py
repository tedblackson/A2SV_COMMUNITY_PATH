class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        indegreeG = [0] * m
        indegreeI = [0] * n
        groupings = defaultdict(list)
        graphI = defaultdict(list)
        graphG = defaultdict(list)
        ans = []
        
        
        for item, before in enumerate(beforeItems):
            if group[item] != -1:
                groupings[group[item]].append(item)
            for ele in before:
                if group[item] != group[ele] :
                    if group[item] != -1:
                        indegreeG[group[item]] += 1
                    else:
                        indegreeI[item] += 1
              
                    if group[ele] != -1 and group[item] != -1:
                        graphG[group[ele]].append(group[item])
                    elif group[ele] == -1 and group[item] != -1:
                        graphG[(ele,)].append(group[item])
                    elif group[ele] != -1 and group[item] == -1:
                        graphG[group[ele]].append((item, ))
                    else:
                        graphG[(ele,)].append((item,))
                elif group[item] == group[ele] == -1:
                    graphG[(ele,)].append((item,))
                    indegreeI[item] += 1


                else:
                    graphI[ele].append(item)
                    indegreeI[item] += 1
        
        queueG = deque()
        
        for i, degree in enumerate(indegreeG):
            if degree == 0:
                queueG.append(i)
        
        for i, degree in enumerate(indegreeI):
            if degree == 0 and group[i] == -1:
                queueG.append((i,))
        
        while queueG:

            
            srcG = queueG.popleft()
            
            if type(srcG) is tuple:
                ans.append(srcG[0])
                
            
            for child in graphG[srcG]:
                if type(child) is tuple:
                    indegreeI[child[0]] -=1
                    if indegreeI[child[0]] == 0:
                        queueG.append(child)
                else:
                    indegreeG[child] -= 1
                    if indegreeG[child] == 0:
                        queueG.append(child)
                
            queueI = deque()
            
            for ele in groupings[srcG]:
                if indegreeI[ele] == 0:
                    queueI.append(ele)
            
            while queueI:
                srcI = queueI.popleft()
                ans.append(srcI)
                
                for child in graphI[srcI]:
                    indegreeI[child] -= 1
                    
                    if indegreeI[child] == 0:
                        queueI.append(child)
        return ans if len(ans) == n else []
                
            
            