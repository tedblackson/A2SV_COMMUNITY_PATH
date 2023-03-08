# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        maximum = -1
        def dfs(root, depth = 0):
            nonlocal maximum
            if root and depth > maximum:
                ans.append(root.val)
            maximum = max(depth, maximum ) if root else maximum
            
        
            if not root:
                return None
            
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        dfs(root)
        return ans
                
        
        

            