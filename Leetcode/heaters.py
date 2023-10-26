class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        n = len(houses)
        m = len(heaters)
        houses.sort()
        heaters.sort()

        def distOne(hoidx, heidx):
            distOne = abs(houses[hoidx] - heaters[heidx])
            return distOne

        def distTwo (hoidx, heidx):
            distTwo = abs(houses[hoidx] - heaters[heidx + 1])
            return distTwo

        _min = 0
        heidx = 0

        for hoidx in range(n):
           
            while  heidx + 1 < m and distOne(hoidx, heidx) >= distTwo(hoidx, heidx):
                heidx += 1
                
            _min = max(distOne(hoidx, heidx), _min)
        

        return _min


        
