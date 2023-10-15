# 21. Merge Two Sorted Lists
# Easy
#You are given the heads of two sorted linked lists list1 and list2.
#
#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
#Return the head of the merged linked list.
#
# 
#
#Example 1:
#
#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#
#Example 2:
#
#Input: list1 = [], list2 = []
#Output: []
#
#Example 3:
#
#Input: list1 = [], list2 = [0]
#Output: [0]
#
# 
#
#Constraints:
#
#    The number of nodes in both lists is in the range [0, 50].
#    -100 <= Node.val <= 100
#    Both list1 and list2 are sorted in non-decreasing order.
#





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list = merged_list_head = ListNode(-1)

        while list1 and list2:
            if list1.val < list2.val:
                next_elem = list1.next
                merged_list.next = list1
                list1 = next_elem
            else:
                next_elem = list2.next
                merged_list.next = list2
                list2 = next_elem

            merged_list = merged_list.next

        if list1:
            merged_list.next = list1
        else:
            merged_list.next = list2

        return merged_list_head.next


