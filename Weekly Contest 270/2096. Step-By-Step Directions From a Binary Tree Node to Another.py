#Reference: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612105/3-Steps

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find_path(root, val, path):
            
            if root.val == val:
                return True #tell the below to proceed with adding 
            
            if root.left and find_path(root.left, val, path): #deep down to left first
                path+='L'
            elif root.right and find_path(root.right, val, path): #then right
                path+='R'

            return path
        
        s, d = [], []
        
        find_path(root, startValue, s)
        find_path(root, destValue, d)
        
        while s and d and s[-1] == d[-1]:
            s.pop()
            d.pop()
        
        return 'U' * len(s) + ''.join(reversed(d))
        
        
            
            