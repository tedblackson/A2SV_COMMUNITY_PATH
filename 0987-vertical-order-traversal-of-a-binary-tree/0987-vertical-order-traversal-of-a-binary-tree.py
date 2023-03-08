# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        count = defaultdict(list)
        
        def dfs(root, row= 0, col = 0):
            
            if not root: return
            
            count[col].append((row, root.val))
            
            dfs(root.left, row + 1, col -1)
            dfs(root.right, row + 1, col + 1)
        dfs(root)
        ans = []
        keys = sorted(list(count.keys()))
        for col in keys:
            count[col].sort()
            temp = []
            
            for ele in count[col]:
                temp.append(ele[1])
            ans.append(temp)
        return ans
            