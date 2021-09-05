#Reference: https://leetcode.com/problems/operations-on-tree/discuss/1444313/Build-Child-Map-and-BFS

from collections import defaultdict, deque

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None] * len(parent)
        
        self.child = defaultdict(list)
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)
            

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != None: return False
        
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user: return False
        
        self.locked[num] = None
        return True
        

    def upgrade(self, num: int, user: int) -> bool:
        
        #check whether ancestor and itself has lock 
        i= num
        while i != -1:
            if self.locked[i] !=None: return False #if there's a lock
            i = self.parent[i]
            
        #check whether descendants have locks
        
        locked_count, q = 0, deque([num])
        
        while q:
            j = q.popleft()
            
            if self.locked[j] != None:
                self.locked[j] = None
                locked_count+=1
            
            q.extend(self.child[j])
            
        if locked_count > 0:
            self.locked[num] = user
        return locked_count > 0
        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)