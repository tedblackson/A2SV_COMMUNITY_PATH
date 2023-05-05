class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.tree = defaultdict(list)
        self.locked = {}
        for child in range(1, len(parent)):
            self.tree[parent[child]].append(child)
        
            
        

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user 
            return True
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        val = self.locked.get(num)
        if val == user:
            del self.locked[num]
            return True
        return False
            
        
        

    def upgrade(self, num: int, user: int) -> bool:
        if  self.checkAncestor(num) and self.hasOne(num) and self.lock(num, user):
            self.unlockDescendant(num, None)
            return True

        return False
        
    def checkAncestor(self, root):
        if root in self.locked:
            return False
        if root == -1:
            return True
        return self.checkAncestor(self.parent[root])
        
    def hasOne(self, root):
        if root in self.locked:
            return True
        for child in self.tree[root]:
            if self.hasOne(child):
                return True
        
        
    def unlockDescendant(self, parent, root):
        if parent in self.locked and root != None: 
            del self.locked[parent]
        
        for child in self.tree[parent]:
            self.unlockDescendant(child, parent)
            
            
            


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)