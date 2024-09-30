# 729. My Calendar I
# Medium
#
#    You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
#
#    A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
#
#    The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
#
#    Implement the MyCalendar class:
#
#        MyCalendar() Initializes the calendar object.
#        boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
#
#
#
#    Example 1:
#
#    Input
#    ["MyCalendar", "book", "book", "book"]
#    [[], [10, 20], [15, 25], [20, 30]]
#    Output
#    [null, true, false, true]
#
#    Explanation
#    MyCalendar myCalendar = new MyCalendar();
#    myCalendar.book(10, 20); // return True
#    myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
#    myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
#
#
#
#    Constraints:
#
#        0 <= start < end <= 109
#        At most 1000 calls will be made to book.
#


class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:

        def findPoint(start):
            low, high = 0, len(self.events)-1
            while low <= high:
                mid = (low + high) // 2
                if self.events[mid][0] > start:
                    high = mid-1
                elif self.events[mid][0] <= start and (mid == len(self.events)-1 or self.events[mid+1][0] > start):
                    return mid
                else:
                    low = mid+1

            return -1

        prev = findPoint(start)
        if prev != -1 and  self.events[prev][1] > start:
                #print(f"fail {start},{end}")
                return False
        if (prev+1) < len(self.events):
            nxt = self.events[prev+1]
            if end > nxt[0]: # and end < nxt[1]:
                #print(f"fail2 {start},{end}")
                return False

        #print(f"ins: {start},{end} at {prev}")
        self.events.insert(prev+1, (start, end))
        #print(self.events)

        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
