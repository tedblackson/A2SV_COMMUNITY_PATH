# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        ans = []
        to_delete = set(to_delete)
        def dfs(root):
            if not root:
                return 
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if not left:
                root.left = None
            if not right:
                root.right = None
                

            if root.val in to_delete:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return False
            else:
                return True
        if dfs(root):
            ans.append(root)
        
            

        


        return ans
        
            
            
                
