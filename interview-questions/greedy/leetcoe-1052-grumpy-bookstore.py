#1052. Grumpy Bookstore Owner
#Medium
#
#    There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
#
#    On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#
#    When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
#
#    The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
#
#    Return the maximum number of customers that can be satisfied throughout the day.
#
#
#
#    Example 1:
#
#    Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
#    Output: 16
#    Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
#    The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
#
#    Example 2:
#
#    Input: customers = [1], grumpy = [0], minutes = 1
#    Output: 1
#
#
#
#    Constraints:
#
#        n == customers.length == grumpy.length
#        1 <= minutes <= n <= 2 * 104
#        0 <= customers[i] <= 1000
#        grumpy[i] is either 0 or 1.
#
#


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        if len(customers) <= minutes:
            return sum(customers)

        total = sum(customers[0:minutes])
        gain = sum(map(lambda cur : cur[0] if grumpy[cur[1]] == 1 else 0, zip(customers[0:minutes], range(0,minutes))))

        low, high = 0, minutes
        max_total, max_gain, max_gain_pos = total, gain, 0

        while high < len(customers):
            if grumpy[low] == 1:
                gain -= customers[low]
            if grumpy[high] == 1:
                gain += customers[high]

            total -= customers[low]
            total  += customers[high]

            if gain > max_gain:
                max_gain = gain
                max_total = total
                max_gain_pos = low+1


            low += 1
            high += 1

        to_add = sum(map(lambda cur : cur[0] if (cur[1] < max_gain_pos or cur[1] >= max_gain_pos + minutes) and grumpy[cur[1]] == 0 else 0, zip(customers, range(0,len(customers)))))
        print(max_total, to_add)
        return max_total + to_add
