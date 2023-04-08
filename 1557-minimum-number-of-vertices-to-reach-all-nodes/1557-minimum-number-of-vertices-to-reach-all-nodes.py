class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for source, dest in edges:
            graph[dest].append(source)
        
        ans = []
        for i in range(n):
            if i not in graph:
                ans.append(i)
        return ans
                