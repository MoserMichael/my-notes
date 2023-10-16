# 92. Reverse Linked List II
# Medium
#Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
#
#
#
#Example 1:
#
#Input: head = [1,2,3,4,5], left = 2, right = 4
#Output: [1,4,3,2,5]
#
#Example 2:
#
#Input: head = [5], left = 1, right = 1
#Output: [5]
#
#
#
#Constraints:
#
#    The number of nodes in the list is n.
#    1 <= n <= 500
#    -500 <= Node.val <= 500
#    1 <= left <= right <= n
#
#
#Follow up: Could you do it in one pass?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        self.before_left_link = None

        ret = self.recursive(head, 1, left, right)

        if self.before_left_link:
            self.before_left_link.next = self.right_link

        self.left_link.next = self.after_right_link

        if not self.before_left_link:
            return self.right_link
        return head

    def recursive(self, node, cur_idx, left, right):

        print(f"{cur_idx} left: {left} right: {right}")
        if cur_idx == left - 1:
            self.before_left_link = node
        elif cur_idx == left:
            self.left_link = node
        elif cur_idx == right:
            self.right_link = node
        if cur_idx == right+1:
            self.after_right_link = node

        if not node:
            return None

        ret = self.recursive(node.next, cur_idx+1, left, right)


        if cur_idx >= left and cur_idx <= right:
            node.next = None
            if cur_idx != right and ret:
                ret.next = node

        return node

