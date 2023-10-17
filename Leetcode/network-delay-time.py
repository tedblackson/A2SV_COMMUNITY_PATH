class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        
        
        for src, dest, weight in times:
            graph[src].append((dest, weight))
            

        
        start = (0, k)
        
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        visited = set()
        
        heap = [start]
        
        while heap:
            
            curdist , curnode = heappop(heap)

            if curnode in visited: continue

            visited.add(curnode)
            for neighbor , weight in graph[curnode]:
                if curdist + weight < distances[neighbor]:
                    distances[neighbor] = curdist + weight
                    heappush(heap, (curdist + weight, neighbor))
            
                
        
        ans = max(distances[1:])

        
        return -1 if ans == float('inf') else ans

        
        