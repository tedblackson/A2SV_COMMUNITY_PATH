# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = [0]
        visited = set()
        def dfs(root, prev, cur):
            
            if not root:
                if prev not in visited and not(prev.left or prev.right):
                    visited.add(prev)
                    ans[0] += int(cur)
                return 
            cur += str(root.val)
            dfs(root.left, root, cur)
            dfs(root.right, root, cur)
        dfs(root, None, "")
        return int(ans[0])
    
            