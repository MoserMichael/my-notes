# 82. Remove Duplicates from Sorted List II
# Medium
#    Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
#
#
#
#    Example 1:
#
#    Input: head = [1,2,3,3,4,4,5]
#    Output: [1,2,5]
#
#    Example 2:
#
#    Input: head = [1,1,1,2,3]
#    Output: [2,3]
#
#
#
#    Constraints:
#
#        The number of nodes in the list is in the range [0, 300].
#        -100 <= Node.val <= 100
#        The list is guaranteed to be sorted in ascending order.
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1, head)

        prev = head
        slow = head.next
        fast = head.next
        diff = 0
        while fast:
            if fast.val == slow.val:
                diff += 1
            else:
                if diff > 1:
                    prev.next = fast
                    slow = fast
                else:
                    prev = slow
                    slow = fast
                diff = 1

            fast = fast.next

        if diff  > 1:
            prev.next = None

        return head.next
