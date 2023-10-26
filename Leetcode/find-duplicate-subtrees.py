# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        

        count = defaultdict(int)

        def dfs(root):

            if not root:
                return ""
            
            left = "L" + dfs(root.left)
            right =  "R" + dfs(root.right)
            ans = str(root.val) + left + right
            if count[ans] != -1:
                count[ans] += 1

                if count[ans] > 1 :
                    res.append(root)
                    count[ans] = -1
            return ans
        
        res = []
        dfs(root)
        return res