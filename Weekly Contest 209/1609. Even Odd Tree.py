#Reference: https://leetcode.com/problems/even-odd-tree/discuss/877739/Clean-Python-3-queue-O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        is_even = True #level 0
        
        while queue:
            prev= None
            
            for _ in range(len(queue)): #same level
                node = queue.popleft()
                
                if is_even:
                    if node.val % 2 == 0: return False
                    if prev and prev >= node.val: return False
                else:
                    if node.val % 2 == 1: return False
                    if prev and prev <= node.val: return False
                
                prev = node.val
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
            is_even = not is_even
                
        return True
                    
                    
                
            
                
            
        
            
            
            