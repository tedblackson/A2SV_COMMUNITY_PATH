# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        def insertNode(root, val):
            
            if not root:
                return TreeNode(val)
            
            elif val < root.val:
                root.left = insertNode(root.left, val)
            else:
                root.right = insertNode(root.right, val)
            return root
        insertNode(root, val)
        return root
            
            
            