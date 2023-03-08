# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        def dfs(current, ans):
            
            if not current:
                ans.append(None)
                return None
            
            ans.append(current.val)
            dfs(current.left, ans)
            dfs(current.right, ans)
        dfs(p, ans1)
        dfs(q, ans2)
        
        
        return ans1 == ans2
        