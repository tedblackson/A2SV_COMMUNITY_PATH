class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        queue = deque()
        answer = [(math.inf, 0)] * len(quiet)
        graph = defaultdict(list)
        
        indegree = [0] * len(quiet)
        for more, less in richer:
            graph[more].append(less)
            indegree[less] += 1
        
        for person, val in enumerate(indegree):
            if not val:
                answer[person] = (quiet[person], person)
                queue.append(person)
                
        while queue:
            src = queue.popleft()
            for child in graph[src]:
                answer[child] = min((quiet[child], child), answer[src], answer[child])
                indegree[child] -= 1
                
                if not indegree[child]:
                    queue.append(child)
            
        answer = [ele[1] for ele in answer]
        return answer
            