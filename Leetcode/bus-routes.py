class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        busStops = defaultdict(list)
        
        for bus, route in enumerate(routes):
            for busStop in route:
                busStops[busStop].append(bus)
                
    
        queue = deque((source,))
        visitedBuses = set()
        visitedStops = {source,}
        level = 0
        
        if source == target:
            return 0
        
        while queue:
            
            
            for _ in range(len(queue)):
                
                src = queue.popleft()

                for bus in busStops[src]:
                    if bus not in visitedBuses:
                        visitedBuses.add(bus)
                        for stop in routes[bus]:
                            
                            
                            if stop not in visitedStops:
                                if stop == target:
                                    return level + 1
                                visitedStops.add(stop)

                                queue.append(stop)
            level +=1
            
            
        return -1
            
            
                
        
        
        