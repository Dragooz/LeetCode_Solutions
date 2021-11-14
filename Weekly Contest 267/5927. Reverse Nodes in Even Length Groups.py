# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, headd: Optional[ListNode]) -> Optional[ListNode]:
        
        i = 0
        master_break = True
        head = headd
        
        while master_break:
            i+=1
            
            temp = head
            list_= []

            for j in range(i):
                if not temp: 
                    master_break = False
                    break
                list_.append(temp.val)
                temp = temp.next
            
            if len(list_) % 2== 0:#even reverse
                for k in list_[::-1]:
                    head.val = k
                    if head.next:
                        head = head.next
            else:
                for _ in range(len(list_)):
                    head = head.next


        return headd
                    
            