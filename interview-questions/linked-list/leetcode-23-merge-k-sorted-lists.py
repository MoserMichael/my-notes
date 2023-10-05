# 23. Merge k Sorted Lists
# Hard
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
#Merge all the linked-lists into one sorted linked-list and return it.
#
#
#
#Example 1:
#
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6
#
#Example 2:
#
#Input: lists = []
#Output: []
#
#Example 3:
#
#Input: lists = [[]]
#Output: []
#
#
#
#Constraints:
#
#    k == lists.length
#    0 <= k <= 104
#    0 <= lists[i].length <= 500
#    -104 <= lists[i][j] <= 104
#    lists[i] is sorted in ascending order.
#    The sum of lists[i].length will not exceed 104.
#


import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Elm:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return Solution.mergeIt(lists)

    @staticmethod
    def mergeIt(lists):

        smallest_heap = []
        first_node = last_node = None

        for elm in lists:
            if elm is not None:
                heapq.heappush( smallest_heap, Elm(elm) )

        while len(smallest_heap) != 0:
            elm = heapq.heappop(smallest_heap)
            list_elm = elm.node

            #print(f"-> {list_elm.val}")
            if not first_node:
                first_node = last_node = list_elm
            else:
                last_node.next = list_elm
                last_node = list_elm

            list_elm = list_elm.next

            if list_elm is not None:
                new_elm = Elm(list_elm )
                heapq.heappush( smallest_heap, new_elm )

        if last_node is not None:
            last_node.next = None

        return first_node










