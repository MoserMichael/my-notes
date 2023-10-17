# 61. Rotate List
# Medium
#Given the head of a linked list, rotate the list to the right by k places.
#
#
#
#Example 1:
#
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]
#
#Example 2:
#
#Input: head = [0,1,2], k = 4
#Output: [2,0,1]
#
#
#
#Constraints:
#
#    The number of nodes in the list is in the range [0, 500].
#    -100 <= Node.val <= 100
#    0 <= k <= 2 * 109



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return Solution.norecursion(head, k)
        #return self.recursive(head, k)

    def norecursion(head, k):
        # count entries
        count = 0
        count_link = head
        while count_link:
            count += 1
            if not count_link.next:
                count_link.next = head
                break
            count_link = count_link.next

        if not count:
            return head

        break_at = count - k % count
        cur = head
        for idx in range(1, break_at):
            cur = cur.next

        ret = cur.next
        cur.next = None
        return ret

    def recursive(self, head, k):

        #if k == 0 or head is None:
        #    return head

        self.at_before_rotate = None

        self.walkRec(head, k, 1)
        if not self.at_before_rotate:
            return head

        self.at_before_rotate.next = None
        self.last_node.next = head
        return self.at_rotate


    def walkRec(self, node, rotate_at, count):

        if not node:
            return 0,  count - 1, False

        level, count, before_rotate = self.walkRec(node.next, rotate_at, count + 1)

        level += 1
        ret_before_rotate = False

        if before_rotate:
            self.at_before_rotate = node

        if level % count == rotate_at % count:
            self.at_rotate = node
            ret_before_rotate = True

        if level == 1:
            self.last_node = node

        return level, count, ret_before_rotate


