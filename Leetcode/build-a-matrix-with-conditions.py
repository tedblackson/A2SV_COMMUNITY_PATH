class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        graphR = defaultdict(list)
        graphC = defaultdict(list)

        def initiate(conditions, graph):
            indegree = [0] * (k + 1)
            for one, two in conditions:
                graph[one].append(two)
                indegree[two] += 1
                
            return indegree
        
        indegreeR = initiate(rowConditions, graphR)
        indegreeC = initiate(colConditions, graphC)
        

        
        def bfs(queue, graph, indegree):
            ans = []
            while queue:
                src = queue.popleft()
                ans.append(src)
                
                for child in graph[src]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)
            return ans
                        
        
        def search(indegree):
            queue = deque()
            for i, val in enumerate(indegree):
                if i != 0 and val == 0:
                    queue.append(i)
            return queue
        
        queueR = search(indegreeR)
        queueC = search(indegreeC)
        
        
        row_order = bfs(queueR, graphR, indegreeR)
        col_order = bfs(queueC, graphC, indegreeC)
        
        if len(row_order) != k or len(col_order) != k:
            return []
        combine = defaultdict(list)
        
        for i, val in enumerate(row_order):
            combine[val].append(i)
        for i , val in enumerate(col_order):
            combine[val].append(i)
        
        ans = [[0] * k for _ in range(k)]
        for key, (row, col) in combine.items():
            ans[row][col] = key
            
        return ans
            
        
        
                        
                    