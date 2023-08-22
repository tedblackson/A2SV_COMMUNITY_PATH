class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegrees = [0] * n
        visited = set()
        ans = -1
        for par, child in enumerate(edges):
            if child != -1: indegrees[child] += 1
        
        queue = deque()
        for node, val in enumerate(indegrees):
            if val == 0:
                queue.append(node)
                visited.add(node)

        def bfs(queue: deque):
            while queue:
                for _ in range(len(queue)):
                    src = queue.popleft()
                    child = edges[src]

                    if child != -1:
                        indegrees[child] -= 1
                        if child not in visited and indegrees[child] == 0:
                            visited.add(child)
                            queue.append(child)
                        
        
        bfs(queue)

        for node in range(n):
            if node not in visited:
                prev = len(visited)
                visited.add(node)
                indegrees[node] -= 1
                queue.append(node)
                bfs(queue)
                cur = len(visited)
                ans = max(ans, cur - prev)

        return ans if ans > 0 else -1
            




                


