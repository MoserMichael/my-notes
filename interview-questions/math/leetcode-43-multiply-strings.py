# 43. Multiply Strings
# Medium
#
#    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
#    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#    Example 1:
#
#    Input: num1 = "2", num2 = "3"
#    Output: "6"
#
#    Example 2:
#
#    Input: num1 = "123", num2 = "456"
#    Output: "56088"
#
#     
#
#    Constraints:
#
#        1 <= num1.length, num2.length <= 200
#        num1 and num2 consist of digits only.
#        Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sum = []

        if num1 == '0':
            return "0"

        fact = 0
        for idx2 in range(len(num2)-1, -1, -1):
            multiplier = int(num2[idx2])

            if multiplier == 0:
                ret = [0]
            else:
                ret = [0] * fact
                remainder = 0
                for idx in range(len(num1)-1, -1, -1):
                    r = int(num1[idx]) * multiplier + remainder

                    ret.append(r % 10)
                    remainder = r // 10

                if remainder:
                    ret.append(remainder)

            # add ret to sum
            sum = Solution.add(ret, sum)
            fact += 1

        sum.reverse()
        return "".join(map(str,sum))

    def add(v1, v2):
        if len(v1) > len(v2):
            return Solution.add_imp(v1, v2)
        return Solution.add_imp(v2, v1)

    def add_imp(v1, v2):

        ret = []
        remainder = 0
        cnt = min(len(v1), len(v2))

        remainder = 0
        pos = 0
        while pos < cnt:
            r = (remainder + v1[pos] + v2[pos])
            ret.append( r % 10 )
            remainder = r // 10
            pos+=1

        while pos < len(v1):
            r = (remainder + v1[pos])
            ret.append( r % 10 )
            remainder = r // 10
            pos += 1

        if remainder:
            ret.append(remainder)

        return ret
