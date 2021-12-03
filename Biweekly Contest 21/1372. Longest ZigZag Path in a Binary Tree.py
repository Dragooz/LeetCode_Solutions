#Reference: https://leetcode.com/contest/biweekly-contest-21/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: return [-1, -1, -1] #left, right, res
            
            left, right = dfs(root.left), dfs(root.right)
            #left[1] here means left + right to make it valid
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]

        return dfs(root)[-1]
                    
        
        
        
        
        