# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    visited = set()
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root, val):
            if root in self.visited:
                self.ans = root
            else:
                self.visited.add(root)
            if val == root.val:
                return 
            
            
                
            search(root.left if val < root.val else root.right, val)
            
        search(root, p.val)
        search(root, q.val)
        return self.ans
            
            
            
            
        