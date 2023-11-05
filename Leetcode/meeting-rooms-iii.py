class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        """
            # Things we need to keep track of 
            # currently available rooms -- inititally all rooms are available 
            # How to know when a meeting is over and the room is left empty
            # we always would like to take the room with the least room Number
            
            
            # Example 1
            
            n = 2 
            meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
            
            occupied = 0
            
            rooms = [0, 0]  occ = 0 inititally
            rooms = [10, 0] occ = 1 i =0  [1, 0]
            rooms = [10, 5] occ = 2 i = 1 [1, 1]
            rooms = [10, 10] occ = 2 i = 1 [1, 2]
            rooms = [11] occ = 1 i = 1 [2, 2]
        
        """
        
        vacant = [i for i in range(n)]
        heapify(vacant)
        booked = []
        rooms = [0] * n
    
        
        meetings.sort()

        for start, end in meetings:
            
        
            
            while booked and booked[0][0] <= start:
                _ , room = heappop(booked)
                heappush(vacant, room)
                
            
                
            if vacant:
                room = heappop(vacant)
                heappush(booked, [end, room])
                
            else:
                latest , room = heappop(booked)
                latest += end - start
                heappush(booked, [latest, room])
                
            
            rooms[room] += 1
                    
 
        
        ans = _max = 0
        for i, val in enumerate(rooms):
            
            if val > _max :
                ans =  i
                _max = val
        return ans
        
        