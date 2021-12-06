# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n = 1
        test_len = head
        
        while test_len.next:
            test_len = test_len.next
            n+=1
        
        if n == 1:
            return 
        
        modify = head
        for _ in range((n//2)- 1):
            modify = modify.next
        
        if (n//2) + 2 <= n:
            modify.next = modify.next.next
        else:
            modify.next = None
        
        return head