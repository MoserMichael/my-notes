# 343. Integer Break
# Medium
#
#    Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
#
#    Return the maximum product you can get.
#
#
#
#    Example 1:
#
#    Input: n = 2
#    Output: 1
#    Explanation: 2 = 1 + 1, 1 × 1 = 1.
#
#    Example 2:
#
#    Input: n = 10
#    Output: 36
#    Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
#
#
#    Constraints:
#
#        2 <= n <= 58


class Solution:
    def integerBreak(self, n: int) -> int:

        tmp_arr = [1] * (n+1)

        for idx in range(2, (n+1)):
            max_prod = idx-1

            #print(f"idx {idx}")

            for idx_inner in range(1, idx):

                prod = max(idx_inner,tmp_arr[idx_inner]) * max(idx-idx_inner, tmp_arr[idx-idx_inner])
                max_prod = max(max_prod, prod)

                #print(f"-> idx {idx} idx_inner {idx_inner} prod {prod} max_prod {max_prod}")

            tmp_arr[idx] = max_prod

        #print(tmp_arr)
        return tmp_arr[n]

