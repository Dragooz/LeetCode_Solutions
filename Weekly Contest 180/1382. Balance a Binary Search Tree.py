#Reference: https://leetcode.com/problems/balance-a-binary-search-tree/discuss/540038/python-3-easy-to-understand

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        #make it into a vine, clean list
        v = []
        
        def dfs(node):
            if node:
                dfs(node.left) #get the smallest
                v.append(node.val) #record
                dfs(node.right) #get the same level right val
                
        dfs(root)
        
        #make it re-organize
        
        def bst(v):
            if not v:
                return None
            
            mid = len(v) // 2
            ans = TreeNode(v[mid])
            ans.left = bst(v[:mid])
            ans.right = bst(v[mid+1:]) #skip the middle val
            
            return ans
        
        return bst(v)
            
            
            
                