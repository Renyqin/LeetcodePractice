# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        p1 = head
        p2 = head
        
        if not p1 or not p1.next or not p2.next.next:
            return False
        
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next.next
            
            if not p2 or not p2.next:
                return False
            
            if p1 == p2:
                return True
            
            

        return False
            
            