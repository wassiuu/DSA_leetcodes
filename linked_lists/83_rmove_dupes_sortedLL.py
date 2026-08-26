'''
Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = head 
        while dummy and dummy.next:
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return head
        