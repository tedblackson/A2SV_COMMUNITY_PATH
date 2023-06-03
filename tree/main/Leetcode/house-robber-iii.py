# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def robHouse(root):
            
            if not root:
                return 0
            
            one = robHouse(root.right.right) if root.right else 0
            two = robHouse(root.right.left) if root.right else 0
            three = robHouse(root.left.left) if root.left else 0
            four = robHouse(root.left.right) if root.left else 0
            
            five = robHouse(root.right)
            six = robHouse(root.left)
            
            choice_one = root.val + one + two + three + four
            choice_two = five + six
            
            return max(choice_one, choice_two)
        
        return robHouse(root)
    
    
            
            