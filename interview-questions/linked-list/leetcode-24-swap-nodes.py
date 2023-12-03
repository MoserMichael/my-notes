# 24. Swap Nodes in Pairs
# Medium
#
#    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#
#
#    Example 1:
#
#    Input: head = [1,2,3,4]
#    Output: [2,1,4,3]
#
#    Example 2:
#
#    Input: head = []
#    Output: []
#
#    Example 3:
#
#    Input: head = [1]
#    Output: [1]
#
#
#
#    Constraints:
#
#        The number of nodes in the list is in the range [0, 100].
#        0 <= Node.val <= 100
#



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return Solution.rec(head)

    def rec(node):
        if not node:
            return None

        next_node = node.next

        if not next_node:
            return node

        after_next = next_node.next

        next_node.next = node
        node.next = Solution.rec(after_next)

        return next_node

