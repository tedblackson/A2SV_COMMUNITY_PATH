# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        count = defaultdict(lambda : [math.inf, -math.inf])
        
    
        maximum = 0
        
        def dfs(root, row = 0, col = 1):
            
            if not root: return 
            
            count[row][-1] = max(count[row][-1], col)
            count[row][0] = min(count[row][0], col)
            
            dfs(root.left, row + 1 , col * 2 - 1 )
            dfs(root.right, row + 1, col * 2 )
        dfs(root)
        
        for row in count:
            if len(count[row]) == 1:
                maximum = max(maximum, 1)
            else:
                maximum = max(maximum, count[row][-1] - count[row][0] + 1)
        return maximum
                
        
        
        
     
        
        
        
    
            
        
        
        
                