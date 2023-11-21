# 118. Pascal's Triangle
# Easy
#Given an integer numRows, return the first numRows of Pascal's triangle.
#
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
#Example 1:
#
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#Example 2:
#
#Input: numRows = 1
#Output: [[1]]
#
#
#
#Constraints:
#
#    1 <= numRows <= 30
#


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows < 1:
            return []

        ret = []
        cur = [1]

        for idx in range(1, numRows+1):
            next = [0] * (idx+1)
            next[0]=1
            next[len(next)-1]=1
            for j in range(0, len(cur)):
                s = cur[j]
                if (j+1) < len(cur):
                    s += cur[j+1]
                next[j+1] = s
            ret.append(cur)
            cur = next

        return ret
