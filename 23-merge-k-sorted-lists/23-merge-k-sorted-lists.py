# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans_node = ListNode()
        head = ans_node
        q = []
        count = 0 
        for node in lists:
            while node:
                #print(node.val)
                #print(node)
                heapq.heappush(q, (node.val,count, node))
                node = node.next
                count+=1
            
                
        while q:
            ele = heapq.heappop(q)
            ans_node.next = ele[-1]
            ans_node = ans_node.next

            
        return head.next
            
        