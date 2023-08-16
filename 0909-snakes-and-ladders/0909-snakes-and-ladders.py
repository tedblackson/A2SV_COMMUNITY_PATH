class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        
        mapper = {}
        flag = True
        cur = 1
        row = n -1
        col = 0
        for _ in range(n):
            for _ in range(n):
                
                mapper[cur] = (row, col)
                if (col == 0 and not flag) or (col == n -1 and flag):
                    row -=1
                    flag = not flag
                elif flag:
                    col +=1
                else:
                    col -=1
                    
                cur += 1
                    
        
        
        queue = deque((1,))
        visited = set((1,))
        level = 0
        
        while queue:
            # print(queue)
            # print(visited)
            for _ in range(len(queue)):
                               
                cur = queue.popleft()
                
                if mapper[n **2] == mapper[cur]:
                    return level
                
                for choice in range( cur + 1, min( cur + 6, n ** 2 ) + 1):
                    row, col = mapper[choice]
                    
                    if choice not in visited:
                        visited.add(choice)

                        if board[row][col] != -1 :
                            queue.append(board[row][col])
                        
                        else:
                            queue.append(choice)
              

                    
            level += 1
            
        return -1
                    
        
        
           
                
                    
                    
                
        