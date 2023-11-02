class DetectSquares:

    def __init__(self):
        self.graph = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.graph:
            self.graph[tuple(point)] += 1
        else:
            self.graph[tuple(point)] = 1
        


    def count(self, point: List[int]) -> int:
        x, y = point
        cnt = 0

        for (x1, y1), freq in self.graph.items():
            _x , _y = abs(x - x1), abs(y - y1)

            if _x == _y and _y > 0:
                
                cnt += freq * self.graph.get((x1, y), 0) * self.graph.get((x, y1), 0)

        return cnt
            
 

                






        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)