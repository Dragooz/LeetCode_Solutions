# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        critical_points = []
        index = 1
        while head.next.next:
            prev = head.val
            head = head.next
            next_ = head.next.val
            
            if prev != None and next_!=None:
                if (head.val >prev and head.val > next_) or (head.val <prev and head.val < next_):
                    critical_points.append(index)
                    
            index+=1
        if len(critical_points) >=2: #valid
            return[min(b-a for b, a in zip(critical_points[1:], critical_points[0:-1])), critical_points[-1] - critical_points[0]]
        else:
            return [-1,-1]
        
                