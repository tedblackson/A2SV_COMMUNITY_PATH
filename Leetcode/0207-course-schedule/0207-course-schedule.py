class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        order = []
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for child , parent in prerequisites:
            graph[parent].append(child)
            indegrees[child] += 1
            
            
        queue = deque()
        
        for node, val in enumerate(indegrees):
            if not val:
                queue.append(node)
        
        while queue:
            src = queue.popleft()
            order.append(src)
            
            for child in graph[src]:
                indegrees[child] -=1
                if indegrees[child] == 0:
                    queue.append(child)
        if len(order) != numCourses:
            return False
        return True
            
        
