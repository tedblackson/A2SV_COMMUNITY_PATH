class Solution:
    # The Time Complexity is O(N)
    # The Space Complexity is O(N)
    
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        cpTasks = [ (task[0], task[1], ctr) for ctr, task in enumerate(tasks)]
        nonProcessed = set(cpTasks)
        availTasks = []
        cpTasks.sort()
        time, ctr = cpTasks[0][0] , 0

        order = []
        
        while nonProcessed or availTasks:
            
            while ctr < len(cpTasks) and cpTasks[ctr][0] <= time:
                heappush(availTasks, (cpTasks[ctr][1], cpTasks[ctr][2], cpTasks[ctr][0]))
                nonProcessed.remove((cpTasks[ctr]))
                ctr += 1
            
            
            if availTasks: 
                current = heappop(availTasks)
                order.append(current[1])
                time += current[0]
            else:
                time = cpTasks[ctr][0] 
                
        return order
                                      
                                      
                
            
            
            
        
            
            
            
            
            
        
            
        
        
        
        
        
        
        
        
        
        
            
        
        
        