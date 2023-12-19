# 122. Best Time to Buy and Sell Stock II
# Medium
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
#On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
#
#Find and return the maximum profit you can achieve.
#
#
#
#Example 1:
#
#Input: prices = [7,1,5,3,6,4]
#Output: 7
#Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#Total profit is 4 + 3 = 7.
#
#Example 2:
#
#Input: prices = [1,2,3,4,5]
#Output: 4
#Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#Total profit is 4.
#
#Example 3:
#
#Input: prices = [7,6,4,3,1]
#Output: 0
#Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
#
#
#
#Constraints:
#
#    1 <= prices.length <= 3 * 104
#    0 <= prices[i] <= 104
#


# find local min then local max, add profit between them. then repeat.

class Solution:

    # try to be faster by getting rid of state variable (not much faster)
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        idx = 1
        min_pos = -1

        while idx < len(prices):

            # search for local minimum
            while idx < len(prices):
                if prices[idx-1] < prices[idx]:
                    min_pos = idx-1
                    idx += 1
                    break
                idx += 1

            if min_pos == -1:
                break

            # search for local maximum
            while True:
                if idx == len(prices) or prices[idx-1] > prices[idx]:
                    profit += prices[idx-1] - prices[min_pos]
                    min_pos = -1
                    break
                idx += 1

        return profit

    SEARCH_MIN = 1
    SEARCH_MAX = 2

    # same shit, in terms of performance
    def maxProfitWithStateVar(self, prices: List[int]) -> int:
        profit = 0
        mode = Solution.SEARCH_MIN

        idx = 1
        while idx < len(prices):
            if mode == Solution.SEARCH_MIN:
                if prices[idx-1] < prices[idx]:
                    min_pos = idx-1
                    mode = Solution.SEARCH_MAX

            if mode == Solution.SEARCH_MAX:
                if idx == len(prices)-1 or prices[idx] > prices[idx+1]:
                    profit += prices[idx] - prices[min_pos]
                    mode = Solution.SEARCH_MIN

            idx += 1

        return profit


