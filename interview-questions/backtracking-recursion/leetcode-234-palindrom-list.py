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

#
#    # Intuition
#    Recursive solution can provide O(n) with O(1) memory (if you discard stack space)
#
#    While returning from recursion - maintain the link to the beginning of the list, and advance it as you return from the recursion.
#
#    # Approach
#    Recursivee traversal of the list is in function ```Solution.rec(cur_link, head_link, pos_count):```
#    - ```cur_link``` - the current node, advanced upon calling recursively to the next node
#    - ```head``` - the head of the list, stays the same upon calling recursively
#    - ```pos_count``` - current position in the list (one based), incremented upon calling recursively
#
#    When reaching the end of the list, ``` return True, pos_count, head_link```
#    - True - the status, the list is still considered to be a palindrome
#    - pos_count - the length of the list is returned
#    - head_link - the head of the list, as it was passed
#
#    Upon returning from recursion:
#    - if status is False - no need to check, this is not a palindrom
#    - check if the current node is equal to the head of the list, if not, return False as status
#    - if we are in the second half of the list, compare the value at the head of the list to the value at the current node, if these are not equal then this is not a palindrom.
#    - otherwise: return True for status, return length of list, increment the head position (so that the direct caller will see the next node, in the direction from start to end)
#
#    # Complexity
#    - Time complexity:
#    $$O(n)$$ - passes over each element of the list
#
#    - Space complexity:
#    Add your space complexity here, e.g. $$O(1)$$ - if you discard stack space required for call frames, (if you do not do that, then it's $$O(n)$$)
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stat, _, _ =  Solution.rec(head, head, 1)
        return stat

    def rec(cur_link, head_link, pos_count):
        if not cur_link:
            return True, pos_count, head_link

        status, len, head = Solution.rec(cur_link.next, head_link, pos_count+1)

        if not status:
            return False, -1, None

        if pos_count < len//2:
            return True, len, None

        if head.val != cur_link.val:
            return False, len, None

        return True, len, head.next




