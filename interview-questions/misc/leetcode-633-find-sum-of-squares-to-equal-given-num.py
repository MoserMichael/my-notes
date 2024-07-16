# 633. Sum of Square Numbers
# Medium
#Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
#
#
#
#Example 1:
#
#Input: c = 5
#Output: true
#Explanation: 1 * 1 + 2 * 2 = 5
#
#Example 2:
#
#Input: c = 3
#Output: false
#
#
#
#Constraints:
#
#    0 <= c <= 231 - 1
#



class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return Solution.slowww(c)

    def faster(c):
        # didn't come up with this one, just learning...
        high = int(sqrt(c))
        low = 0

        while high >= low:
            res = high * high + low * low
            if  res == c:
                return True
            if res < c:
                low += 1
            else:
                high -= 1

        return False

    def slowww(c):

        squares = set()
        squares_vec = []
        n=0
        mid = c // 2
        while True:
            sq = n * n
            if sq > c:
                break
            if sq <= mid:
                mid_n = n
            squares_vec.append(sq)
            squares.add(sq)
            n += 1

        for n in range(mid_n+1):
            sq = squares_vec[n]
            m = c-sq
            if m in squares:
                return True
        return False
