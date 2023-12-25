# 225. Implement Stack using Queues
# Easu
#    Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
#
#    Implement the MyStack class:
#
#        void push(int x) Pushes element x to the top of the stack.
#        int pop() Removes the element on the top of the stack and returns it.
#        int top() Returns the element on the top of the stack.
#        boolean empty() Returns true if the stack is empty, false otherwise.
#
#    Notes:
#
#        You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
#        Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
#
#
#
#    Example 1:
#
#    Input
#    ["MyStack", "push", "push", "top", "pop", "empty"]
#    [[], [1], [2], [], [], []]
#    Output
#    [null, null, null, 2, 2, false]
#
#    Explanation
#    MyStack myStack = new MyStack();
#    myStack.push(1);
#    myStack.push(2);
#    myStack.top(); // return 2
#    myStack.pop(); // return 2
#    myStack.empty(); // return False
#
#
#
#    Constraints:
#
#        1 <= x <= 9
#        At most 100 calls will be made to push, pop, top, and empty.
#        All the calls to pop and top are valid.
#
#
#
#    Follow-up: Can you implement the stack using only one queue?
#


class MyStack:

    def __init__(self):
        self.queue_active = []
        self.queue_tmp = []

    def push(self, x: int) -> None:
        self.queue_active.append(x)

    def pop(self) -> int:
        return self._imp(True)

    def top(self) -> int:
        return self._imp(False)

    def _imp(self, do_pop):
        sz = len(self.queue_active)
        ret = None

        for n in range(0, sz):
            first = self.queue_active[0]
            self.queue_active = self.queue_active[1:]

            if n == sz-1:
                ret = first
                if do_pop:
                    break

            self.queue_tmp.append(first)

        tmp = self.queue_active
        self.queue_active = self.queue_tmp
        self.queue_tmp = tmp

        return ret


    def empty(self) -> bool:
        return len(self.queue_active) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
