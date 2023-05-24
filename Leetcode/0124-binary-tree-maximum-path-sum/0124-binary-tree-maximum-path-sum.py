# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        _max = [-math.inf]

        if not root:
            return 0
        
        def dfs(root):
             
                        
            if not root:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            _max[0]  = max(_max[0], left + right + root.val)

            return max(left, right ) + root.val

            
            
        dfs(root)
        return _max[0]
    
    