# 19. Remove Nth Node From End of List
    # Medium
#Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
#Example 1:
#
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]
#
#Example 2:
#
#Input: head = [1], n = 1
#Output: []
#
#Example 3:
#
#Input: head = [1,2], n = 1
#Output: [1]
#
#
#
#Constraints:
#
#    The number of nodes in the list is sz.
#    1 <= sz <= 30
#    0 <= Node.val <= 100
#    1 <= n <= sz
#
#
#
#Follow up: Could you do this in one pass?
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



#    # Intuition
#    it needs to count the nodes from the end, in reverse order.
#     now it is still possible to do it in 'one pass' - recursively, as right recursion.
#
#    (when doing practical work: beware of recursion, as you easily run out of stack space. But this exercise says that there are around 30 nodes)
#
#    # Approach
#
#    Recursive step is in
#         def removeNthRec( node, remove_n):
#    The function receives
#        - The current node
#        - level to remove (remove_n)
#
#     The function returns
#        - the count of the number of nodes (from the end)
#        - node before the deleted node
#
#    Upon return the 'count of nodes from the end' value is incremented
#     if reverse count is equal to remove_n+1 then delete the node after the current node, and return the current node as the 'node before the deleted node'
#
#    Also: create a dummy node before the first node. (this trick makes it easier to ignore edge cases)
#
#    In top level: if the returned node is equal to the dummy node, then the head is supposed to be deleted, so return the node after head, otherwise return the head
#
#    # Complexity
#    - Time complexity: O(n)
#
#    - Space complexity: O(1)
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        _, before_removed = Solution.removeNthRec( dummy, n)

        if dummy == before_removed:
            return head.next

        return head


    def removeNthRec( node, remove_n):
        if not node:
            return 0, None

        cnt, ret = Solution.removeNthRec( node.next, remove_n)
        cnt += 1

        if cnt == remove_n + 1:
            if node.next:
                node.next = node.next.next
            ret = node

        return cnt, ret


