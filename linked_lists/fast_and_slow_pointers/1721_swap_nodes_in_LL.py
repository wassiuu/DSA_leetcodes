'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values 
of the kth node from the beginning and the kth node from the 
end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        first_p = dummy
        second_p = dummy
        val1 = dummy

        for _ in range(k):
            second_p = second_p.next
        val1 = second_p

        while second_p and second_p.next:
            first_p = first_p.next
            second_p = second_p.next
        
        temp = val1.val
        val1.val = first_p.next.val
        first_p.next.val = temp

        return dummy.next