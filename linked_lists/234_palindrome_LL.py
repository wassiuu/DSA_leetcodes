'''
Given the head of a singly linked list, return true if it is 
a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        
        curr = slow
        prev = None 
        while curr:
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node 
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left=left.next
            right = right.next
        return True
    