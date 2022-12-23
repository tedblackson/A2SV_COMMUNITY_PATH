class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = math.inf
        point = -1

        for i, (point1, point2) in enumerate(points):
            distance = math.sqrt((point1 - x)**2 + (point2 - y)**2)
            if distance < ans and (point1 == x or point2 == y):
                ans = distance
                point = i
        return point
            
        