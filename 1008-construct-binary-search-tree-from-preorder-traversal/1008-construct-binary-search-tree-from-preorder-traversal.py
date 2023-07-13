# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        n =len(preorder)
        cur = [1]


        def buildTree( node,  _max, _min):
 
            if not node or cur[0] >= n: return None


            if _min < preorder[cur[0]] < node.val < _max:
                node.left = TreeNode(preorder[cur[0]])
                cur[0] += 1
                buildTree( node.left, node.val, _min)
                buildTree( node , _max , _min)
            
            elif _min < node.val < preorder[cur[0]] < _max:
                node.right = TreeNode(preorder[cur[0]])
                cur[0] += 1

                buildTree( node.right , _max , _min)

                buildTree( node , _max , _min)

            
            
        
        root = TreeNode(preorder[0])

        buildTree(root, math.inf, -math.inf)

        return root