# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        _ans = [0]
        
        def dfs(root, parent=None, gParent=None):
            
            if  not root:
                return
            if gParent != None and gParent.val%2 == 0:
                _ans[0] += root.val
            
            dfs(root.left, root, parent)
            dfs(root.right, root, parent)
        
        dfs(root)
        return _ans[0]
            
        