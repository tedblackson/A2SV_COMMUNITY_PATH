# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        if not root:
            return ans
        
        def dfs(root, arr = [], prev = None ,_sum = 0):
            
            if not root:
                
                if _sum == targetSum and not(prev.left or prev.right):
                    ans.append(arr[:])
                return
                
            arr.append(root.val)
            dfs(root.left, arr, root, _sum + root.val )
            arr.pop()
            if root.right:
                arr.append(root.val)
                dfs(root.right, arr, root, _sum + root.val)
                arr.pop()
        dfs(root)
        return ans
        
                    