'''
Given the head of a sorted linked list, delete all nodes that 
have duplicate numbers, leaving only distinct numbers from the 
original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head 
        
        while curr and curr.next:
            
            if curr.val == curr.next.val:
                #make the curr move to the last dupe (skip all the dupes)
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                #make prev pointer point to the element after the last dupe
                prev.next = curr.next
            else:
                prev = prev.next
            
            curr = curr.next

        
        return dummy.next