# 25. Reverse Nodes in k-Group
# Hard
#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
#You may not alter the values in the list's nodes, only nodes themselves may be changed.
#
#
#
#Example 1:
#
#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]
#
#Example 2:
#
#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]
#
#
#
#Constraints:
#
#    The number of nodes in the list is n.
#    1 <= k <= n <= 5000
#    0 <= Node.val <= 1000
#
#
#
#Follow-up: Can you solve the problem in O(1) extra memory space?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        if k == 1:
            return head

        _, _, cur, _ = Solution.recursive(head, 0, k)

        return cur


    # note! if the last group is not full then it must not be reversed!
    #
    @staticmethod
    def recursive(link, count_mod, mod_size ):

        assert link is not None

        if not link.next:

            # last element is head of group - tell previous group to swap
            if count_mod == 0:
                # cur - group_head - next_group - swap_list
                return None, None, link, True

            # not last element of a group. Only full last groups are swapped
            swap_list = (count_mod + 1) % mod_size == 0

            return link, link, None, swap_list

        next_link, group_head, next_group, swap_list = Solution.recursive(link.next, (count_mod + 1) % mod_size, mod_size)


        if not swap_list:
            if count_mod == 0:
                # last non swapped group starts - tell previous group to swap
                return None, None, link, True
            # continue as is
            return None, None, None, False


        link.next = None

        if not next_link:
            # last element of group
            return link, link, next_group, True

        # swap order between previous and current link
        next_link.next = link

        if count_mod == 0:
            #print(f"start-group me: {link.val} -> {next_group.val if next_group else -1} group_head {group_head.val}")
            link.next = next_group
            return None, None, group_head, True

        return link, group_head, next_group, True


