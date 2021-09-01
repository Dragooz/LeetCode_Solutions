#Reference from: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        first = head
        last = head
        
        for _ in range(k-1):
            first = first.next
        
        null_checker =first
        
        while null_checker.next:
            null_checker = null_checker.next
            last = last.next
            
        first.val, last.val = last.val, first.val
        
        return head