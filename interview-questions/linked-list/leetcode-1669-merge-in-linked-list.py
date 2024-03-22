# 1669. Merge In Between Linked Lists
# Medium
#    You are given two linked lists: list1 and list2 of sizes n and m respectively.
#
#    Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
#
#    The blue edges and nodes in the following figure indicate the result:
#
#    Build the result list and return its head.
#
#
#
#    Example 1:
#
#    Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
#    Output: [10,1,13,1000000,1000001,1000002,5]
#    Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
#
#    Example 2:
#
#    Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
#    Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
#    Explanation: The blue edges and nodes in the above figure indicate the result.
#
#
#
#    Constraints:
#
#        3 <= list1.length <= 104
#        1 <= a <= b < list1.length - 1
#        1 <= list2.length <= 104
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        return Solution.faster(list1, a, b, list2)
        #return Solution.slow(list1, a, b, list2)


    def faster(list1, a, b, list2):
        start = list1

        cur = 0
        while cur != a-1:
            list1 = list1.next
            cur += 1

        insert_at = list1

        while cur != b:
            list1 = list1.next
            cur += 1

        insert_at.next = list2

        while list2.next:
            list2 = list2.next

        list2.next = list1.next

        return start

    def slow(list1, a, b, list2):
        start = list1

        cur = 0
        while cur != a-1:
            list1 = list1.next
            cur += 1

        dummy = ListNode(-1,list1.next)
        list1.next = list2

        while cur != b:
            dummy = dummy.next
            cur += 1

        while list2.next:
            list2 = list2.next

        list2.next = dummy.next

        return start

