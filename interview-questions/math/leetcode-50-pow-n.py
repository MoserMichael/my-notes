# 50. Pow(x, n)
# Medium
#    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
#     
#
#    Example 1:
#
#    Input: x = 2.00000, n = 10
#    Output: 1024.00000
#
#    Example 2:
#
#    Input: x = 2.10000, n = 3
#    Output: 9.26100
#
#    Example 3:
#
#    Input: x = 2.00000, n = -2
#    Output: 0.25000
#    Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
#     
#
#    Constraints:
#
#        -100.0 < x < 100.0
#        -231 <= n <= 231-1
#        n is an integer.
#        Either x is not zero or n > 0.
#        -104 <= xn <= 104
#


class Solution:


    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        y = Solution.byExp(x, abs(n))

        if n < 0:
            y = 1 / y
        return y

    def byExp(x, n):

        prev_pw = 1
        pw = 1

        prev_ex = x
        ex = x

        # find neares power of two
        while pw < n:
           prev_ex = ex
           ex *= ex

           prev_pw = pw
           pw = int(2*pw)

        # check if exact match
        if pw == n:
            return ex

        # if upper bound is nearer to n than lower bound - decrement power
        if n - prev_pw > pw-n:
            # didn't give much in performance either...
            while pw > n:
                ex /= x
                pw -= 1
            return ex

        while prev_pw < n:
            prev_ex *= x
            prev_pw += 1
        return prev_ex

    # thought that would be faster. No, it isn't.
    def byExpNotFaster(x, n):
        prev_pw = 1
        pw = 1

        prev_ex = x
        ex = x

        arr = []

        # find neares power of two
        while pw < abs(n):
           prev_ex = ex
           ex *= ex

           prev_pw = pw
           pw = int(2*pw)

           arr.append( (pw, ex) )


        # check if exact match
        if pw == abs(n):
            return ex

        while pw > abs(n):
            left = pw - abs(n)

            n_add, num_div = Solution.findNearestGrow(arr, left, 0, len(arr)-1)

            if n_add == -1:
                break

            ex /= num_div
            pw -= n_add

        while pw > abs(n):
            ex /= x
            pw -= 1
        return ex


    def findNearestGrow(arr, fnd, low, high):
        if low > high:
            return -1, -1

        mid = (low + high) // 2
        entry = arr[mid]
        if entry[0] <= fnd:
            mid_next = mid + 1
            if mid_next >= len(arr) or entry[0] > fnd:
                return entry
            return Solution.findNearestGrow(arr, fnd, low+1, high)
        return Solution.findNearestGrow(arr, fnd, 0, low-1)









