class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        
        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
        
        ans = 0
        
        for city_one in range(n):
            for city_two in range(city_one + 1, n):
                rank = len(graph[city_one]) + len(graph[city_two]) 
                
                if city_one in graph[city_two]:
                    rank -= 1
                ans = max(ans ,rank )
        
        return ans