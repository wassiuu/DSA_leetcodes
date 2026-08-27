'''
lc 24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and 
return its head. You must solve the problem without 
modifying the values in the list's nodes (i.e., only nodes
themselves may be changed.)
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head 
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next 

            first.next = second.next 
            second.next = first
            current.next = second 

            current = current.next.next 
        
        return dummy.next

