# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    root = None
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = ""
        queue = deque((root,))

        while queue:
            
            for _ in range(len(queue)):
                src = queue.popleft()
                
                if src:
                    serialized += str(src.val) + "|"
                    queue.append(src.left)
                    queue.append(src.right)
                else:
                    serialized += "null|"
        return serialized
        

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split("|")

        root = TreeNode(int(data[0])) if data[0] != "null" else None
        if not root:
            return None

        cur = 1
        queue = deque((root,))
        n = len(data)
        while queue and cur < len(data):
            src = queue.popleft()
            if src:
                left = TreeNode(int(data[cur])) if data[cur] != "null" else None
                right = TreeNode(int(data[cur + 1])) if cur < n - 2 and data[cur + 1] != 'null' else None
                src.left = left
                src.right = right
                queue.append(left)
                queue.append(right)
                cur += 2
        
        return root
            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))