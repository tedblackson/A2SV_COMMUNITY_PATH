# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        count = [0]
        visited = set()
        def dfs(root, _sum):
            if _sum == targetSum:
                count[0] += 1
            if not root:
                return
            if root.left :
                dfs(root.left, _sum + root.left.val if root.left else 0)
                if root.left not in visited:
                    visited.add(root.left)
                    dfs(root.left, root.left.val)
            if root.right:
                dfs(root.right, _sum + root.right.val if root.right else 0)
                if root.right not in visited:
                    visited.add(root.right)
                    dfs(root.right, root.right.val if root.right else 0)
        dfs(root, root.val)
        
        return count[0]
