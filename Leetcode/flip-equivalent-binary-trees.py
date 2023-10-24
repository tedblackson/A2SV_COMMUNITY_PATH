# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        
        def dfs(root1, root2):
            
            if not (root1 or root2):
                return True
            elif not (root1 and root2):
                return False
            
            left1 = dfs(root1.left, root2.left)
            right1 = dfs(root1.right, root2.right)
            
            left2 = dfs(root1.right, root2.left)
            right2 = dfs(root1.left, root2.right)
            
            if root1.val != root2.val:
                return False
            
            return (left1 and right1) or (left2 and right2)
        
            
            
            
            

        
        ans = dfs(root1, root2)
        
        return ans
            
            