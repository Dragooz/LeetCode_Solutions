# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.ans = 0
        self.val = 0
        self.path = []
        
        def dps(node):
            
            self.path.append(node.val)
            
            if node.left:
                dps(node.left)
            if node.right:
                dps(node.right)
                
            if node.val >= max(self.path):
                self.ans+=1
            
            self.path.remove(node.val)
        
        dps(root)
        return self.ans
        
                
            