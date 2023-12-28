# 148. Sort List
# Medium
#
#    Given the head of a linked list, return the list after sorting it in ascending order.
#
#
#
#    Example 1:
#
#    Input: head = [4,2,1,3]
#    Output: [1,2,3,4]
#
#    Example 2:
#
#    Input: head = [-1,5,3,4,0]
#    Output: [-1,0,3,4,5]
#
#    Example 3:
#
#    Input: head = []
#    Output: []
#
#
#
#    Constraints:
#
#        The number of nodes in the list is in the range [0, 5 * 104].
#        -105 <= Node.val <= 105
#
#
#
#    Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
#


#
#    # Intuition
#    First tried quick sort, as it is easier to code, but it did not solve all the test case. This solution ran out of time on almost sorted lists with lots of entries, and lists with lots of repetitions.
#
#    Merge sort has more stable runtime behavior, that's why it's better suited for this exercise.
#
#    I guess that the purpose of this exercise is to make us more aware of the fact that merge sort has more uniform runtime behavior.
#
#    For example if the case is [2, 3, 4, .... 1000000, 1] then quicksort will have quadratic runtime, whereas merge sort is always subdividing the list into two equal parts, and will run in ```O(n log(n))``` time.
#
#    Another case: quicksort isn't very good at sorting lists with many duplicate entries. I first thought that this is the point of this exercise, and removed the dupliates prior to sorting, then put them back after the fact - but that was not the point of this exercise.
#
#    A better approach for having a quick sort that handles lots of repetitions is to handle cases where entries are equal to the pivot element separately, group them togather with the pivot element.
#
#    # Complexity
#    - Time complexity:
#    $$O(nlog(n))$$
#
#    - Space complexity:
#    if you ignore stack space then it's constant,
#
#    However the stack is a real thing, so it is $$O(log(n))$$
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        f = Solution.mergeSort(head)

        # too long for [all sorted - very long] [one smaller than first one]
        #mapDupCount = Solution.countRemoveDup(head)
        #f,_ = Solution.qsort(head)
        #Solution.addDup(f, mapDupCount)

        return f

    def mergeSort(head):

        # end of recursion - simple case
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            slow = slow.next


        # midpoint at slow
        second_half = slow.next
        slow.next = None

        # recursive sort each half
        head = Solution.mergeSort(head)
        second_half = Solution.mergeSort(second_half)


        # merge back
        ret = cur = ListNode()

        while head and second_half:
            if head.val < second_half.val:
                cur.next = head
                cur = head
                head = head.next
            else:
                cur.next = second_half
                cur = second_half
                second_half = second_half.next

        if second_half:
            cur.next = second_half
        elif head:
            cur.next = head
        else:
            cur.next = None

        return ret.next


    def addDup(head, mapDupCount):
        while head:
            if head.val in mapDupCount:
                nhead = head.next
                count = mapDupCount[head.val]

                while count > 0:
                    node = ListNode(head.val, head.next)
                    head.next = node
                    count -= 1

                mapDupCount.pop(head.val)
                head = nhead
            else:
                head = head.next

    def countRemoveDup(head):

        mapDup = {}

        while head:
            if head.next:
                if head.next.val == head.val:
                    head.next = head.next.next
                    mapDup[head.val] = mapDup.setdefault(head.val, 0) + 1
                    continue

            head = head.next

        return mapDup

    def qsort(first):

        if not first or not first.next:
            return [first, first]

        fval = first.val

        out = [ [None, None], [None, None] ]

        cur = first.next

        while cur:
            next = cur.next
            if cur.val < fval:
                Solution.append(cur, out[0])
            else:
                Solution.append(cur, out[1])
            cur = next

        f1,l1 = Solution.qsort(out[0][0])
        f2,l2 = Solution.qsort(out[1][0])

        if l1:
            l1.next = first
            first.next = f2
            return f1, l2 if l2 else first

        first.next = f2
        return first, l2 if l2 else first

