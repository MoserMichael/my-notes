# 341. Flatten Nested List Iterator
# Medium
#
#    You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
#
#    Implement the NestedIterator class:
#
#        NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
#        int next() Returns the next integer in the nested list.
#        boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
#
#    Your code will be tested with the following pseudocode:
#
#    initialize iterator with nestedList
#    res = []
#    while iterator.hasNext()
#        append iterator.next() to the end of res
#    return res
#
#    If res matches the expected flattened list, then your code will be judged as correct.
#
#
#
#    Example 1:
#
#    Input: nestedList = [[1,1],2,[1,1]]
#    Output: [1,1,2,1,1]
#    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
#
#    Example 2:
#
#    Input: nestedList = [1,[4,[6]]]
#    Output: [1,4,6]
#    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
#
#
#
#    Constraints:
#
#        1 <= nestedList.length <= 500
#        The values of the integers in the nested list is in the range [-106, 106].
#
#


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

#
#    # Intuition
#    Maintain a stack of the current position, where each element stands for a nested list
#
#    # Approach
#
#    getNext does all the work:
#
#    The constructor initialies a stack element that points to the original list, the current position is set to -1.
#
#    getNext looks at the last element of the stack, advance the position of the stack element, if it is past the end of the stack than pop it. The end of iteration occurs if the stack is empty.
#
#    if it is not past the end of the stack then we have two options:
#    - either the current element is a list - in this case push the stack to the next level, next level points to the nested list
#    - the current element is not a list. In this case we are done. Remember the element, so we have something to return upon calling getNext
#
#
#    # Complexity
#    - Time complexity:
#    O(n) - pass over each element of input once,
#
#    - Space complexity:
#    O(deoth-of-list-nesting)
#

class StackElm:
    def __init__(self, lst):
        self.lst = lst
        self.index = -1
        #self.num = len(lst)

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [ StackElm(nestedList) ]


    def hasNext(self) -> bool:

        while True:
            last = self.stack[-1]
            last.index += 1

            #if last.index < last.num:
            if last.index < len(last.lst):

                elm_at = last.lst[ last.index ]
                if elm_at.isInteger():
                    self.ret = elm_at
                    return True

                self.stack.append( StackElm(elm_at.getList() ) )

            else:
                self.stack.pop()
                if len(self.stack) == 0:
                    return False


    def next(self) -> int:
        return self.ret



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
