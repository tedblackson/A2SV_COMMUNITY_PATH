class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)

        
        
        for i, (src, dest) in enumerate(edges):
            graph[src].append((dest, succProb[i]))
            graph[dest].append((src, succProb[i]))
            

        
        start = (-1, start_node)
        
        distances = [0] * (n + 1)
        visited = set()
        
        heap = [start]
        
        while heap:
        
            
            curdist , curnode = heappop(heap)
            curdist *= -1
            
            if curnode in visited: continue

            visited.add(curnode)
            for neighbor , weight in graph[curnode]:
                distance = curdist * weight
              
                if  distance > distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(heap, (-1 * distance , neighbor))
        
        return distances[end_node]