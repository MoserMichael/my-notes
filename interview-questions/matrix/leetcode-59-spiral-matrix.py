# 59. Spiral Matrix II
# Medium
#    Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#
#     
#
#    Example 1:
#
#    Input: n = 3
#    Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#    Example 2:
#
#    Input: n = 1
#    Output: [[1]]
#
#     
#
#    Constraints:
#
#        1 <= n <= 20
#


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:


        dirs = [ (1,0), (0,1), (-1,0), (0,-1) ]
        rev =  [ 2, 3, 0, 1]

        row = [0] * n
        mat = [row.copy() for i in range(0,n)]


        x = -1
        y = 0
        direction = 0
        one_side = 0
        count = 1

        while True:
            x += dirs[direction][0]
            y += dirs[direction][1]

            if 0<=x<n and 0<=y<n and mat[y][x] == 0:

                mat[y][x] = count
                count += 1
                one_side += 1

                if count > (n * n):
                    return mat


            else:

                x += dirs[ rev[direction] ][0]
                y += dirs[ rev[direction] ][1]

                one_side = 0
                direction = (direction+1) % len(dirs)








