class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        graph = defaultdict(list)
        distances = [float('inf')] * n
        stops = [0] * n

        
        for source, dest, weight in flights:
            graph[source].append(( dest, weight))
            
        
        heap = [[-1, 0, src]]
        distances[src] = 0
        
        while heap:
            
            stop, curdist, curnode = heappop(heap)
            
            if stop == k: continue
            
        
            for neighbor , weight in graph[curnode]:
                
                distance = weight + curdist
            
                if stop < k and  distance < distances[neighbor]:
    
                    distances[neighbor] = distance
                    heappush(heap, (stop + 1, distance, neighbor))
            
              
        return distances[dst] if distances[dst] != float('inf') else -1 
                    

                    
                
                
                