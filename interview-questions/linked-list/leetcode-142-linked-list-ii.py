# 142. Linked List Cycle II
# Medium
#    Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
#    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
#
#    Do not modify the linked list.
#
#
#
#    Example 1:
#
#    Input: head = [3,2,0,-4], pos = 1
#    Output: tail connects to node index 1
#    Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
#    Example 2:
#
#    Input: head = [1,2], pos = 0
#    Output: tail connects to node index 0
#    Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
#    Example 3:
#
#    Input: head = [1], pos = -1
#    Output: no cycle
#    Explanation: There is no cycle in the linked list.
#
#
#
#    Constraints:
#
#        The number of the nodes in the list is in the range [0, 104].
#        -105 <= Node.val <= 105
#        pos is -1 or a valid index in the linked-list.
#
#
#
#    Follow up: Can you solve it using O(1) (i.e. constant) memory?
#



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return Solution.constMemory(head)
        #return Solution.fastWithSetOfLoopNodes(head)
        #return Solution.fastWithSetOfNodesSoFar(head)

    def constMemory(head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast:
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if fast == slow:
                # has loop. Now find the start of the loop
                start = head 
                while True:
                    # loop once.
                    cur = fast.next
                    while True:
                        if cur == start:
                            return start
                        if cur == fast:
                            break
                        cur = cur.next
                    start = start.next
                # eof find loop

            slow = slow.next

        return None        

    def fastWithSetOfLoopNodes(head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast:
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if fast == slow:
                # has loop. Now find the start of the loop

                # record loop nodes into set
                loopNodes = set()
                cur = fast.next
                while True:
                    loopNodes.add(cur)
                    if cur == fast:
                        break
                    cur = cur.next

                # loop from start, check if node is in set of loop nodes
                start = head
                while True:
                    if start in loopNodes:
                        return start
                    start = start.next

                # eof find loop

            slow = slow.next

        return None

    def fastWithSetOfNodesSoFar(head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        set_of_nodes = set()

        while cur:
            if cur in set_of_nodes:
                return cur
            set_of_nodes.add(cur)
            
            cur = cur.next
        return None

