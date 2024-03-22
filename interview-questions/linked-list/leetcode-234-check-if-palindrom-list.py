# 234. Palindrome Linked List
# Easy
#
#    Given the head of a singly linked list, return true if it is a
#    palindrome
#    or false otherwise.
#
#     
#
#    Example 1:
#
#    Input: head = [1,2,2,1]
#    Output: true
#
#    Example 2:
#
#    Input: head = [1,2]
#    Output: false
#
#     
#
#    Constraints:
#
#        The number of nodes in the list is in the range [1, 105].
#        0 <= Node.val <= 9
#
#     
#    Follow up: Could you do it in O(n) time and O(1) space?
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # length of list
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        if list_len == 1:
            return True

        # reverse half of the list
        half_list = list_len // 2
        n=0
        prev = None
        cur = head
        while n < half_list:
            next_l = cur.next
            cur.next = prev
            prev = cur
            cur = next_l
            n+=1

        if list_len %2 == 1:
            next_l = next_l.next

        while next_l:
            if next_l.val != prev.val:
                return False
            next_l = next_l.next
            prev = prev.next

        return True

