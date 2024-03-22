# 206. Reverse Linked List
# Easy
#Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#
#Example 1:
#
#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]
#
#Example 2:
#
#Input: head = [1,2]
#Output: [2,1]
#
#Example 3:
#
#Input: head = []
#Output: []
#
#
#
#Constraints:
#
#    The number of nodes in the list is the range [0, 5000].
#    -5000 <= Node.val <= 5000
#
#
#
#Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # non recursive solution. still not much faster
        cur, ret = head, None
        while cur:
            #old_next = cur.next
            #cur.next = ret
            old_next, cur.next = cur.next, ret

            #ret = cur
            #cur = old_next
            ret, cur = cur, old_next

        return ret

    # recursive solution
    def rec(head):
        if not head:
            return None
        head, _ = Solution.imp(head)
        return head

    @staticmethod
    def imp(head):
        if not head.next:
            return head, head

        newHead, tail = Solution.imp(head.next)

        tail.next = head
        head.next = None

        return newHead, head


