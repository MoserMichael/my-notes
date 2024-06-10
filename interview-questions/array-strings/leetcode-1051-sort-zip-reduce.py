# 1051. Height Checker
# Easy
#A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
#
#You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
#
#Return the number of indices where heights[i] != expected[i].
#
#
#
#Example 1:
#
#Input: heights = [1,1,4,2,1,3]
#Output: 3
#Explanation:
#heights:  [1,1,4,2,1,3]
#expected: [1,1,1,2,3,4]
#Indices 2, 4, and 5 do not match.
#
#Example 2:
#
#Input: heights = [5,1,2,3,4]
#Output: 5
#Explanation:
#heights:  [5,1,2,3,4]
#expected: [1,2,3,4,5]
#All indices do not match.
#
#Example 3:
#
#Input: heights = [1,2,3,4,5]
#Output: 0
#Explanation:
#heights:  [1,2,3,4,5]
#expected: [1,2,3,4,5]
#All indices match.
#
#
#
#Constraints:
#
#    1 <= heights.length <= 100
#    1 <= heights[i] <= 100
#

#python3 one liner, explained and illustrated
#
#Lets produce a list of pairs, where each element of the sorted array is paired with the element from the original array.
#
#<pre><code>
#>>> heights = [1,1,4,2,1,3]
#>>> list( zip( sorted(heights), heights) )
#[(1, 1), (1, 1), (1, 4), (2, 2), (3, 1), (4, 3)]
#</code></pre>
#
#Note the `list( .. )` conversion is just to show the content of the result of `zip`
#
#Now the argument function of `reduce` takes a tuple from the paired list. The function adds a one, if the first element of the tuple, coming from the sorted list, is different to the second element of the tuple, where the second element comes from the input list
#
#`lambda prev, cur : prev + (1 if cur[0] != cur[1] else 0)`
#
#Now the reduce function, it returns the sum of calling the function on all elements of the paired values.
#
#`return reduce( lambda prev, cur : prev + (1 if cur[0] != cur[1] else 0), zip(sorted(heights), heights), 0 )`
#`
#The application of reduce to the example can be illustrated as follows:
#
#<pre><code>
#>>> lst=[(1, 1), (1, 1), (1, 4), (2, 2), (3, 1), (4, 3)]
#>>>
#>>> f=lambda prev, cur : prev + (1 if cur[0] != cur[1] else 0)
#>>>
#>>> f( f( f( f( f( f(0, lst[0]), lst[1]), lst[2]), lst[3]), lst[4]), lst[5])
#</code></pre>
#
#That's why the `reduce` function reminds me of the nested matryoshka doll...
#![russian dolls cropped for RR10.jpg](https://assets.leetcode.com/users/images/97170b55-7501-4a2d-840b-f583eefdb53e_1717983286.7584877.jpeg)
#


from functools import reduce

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return reduce( lambda prev, cur : prev + (1 if cur[0] != cur[1] else 0), zip(sorted(heights), heights), 0 )

    def solve(heights):
        h = heights.copy()
        h.sort()
        ret = 0
        for idx,v in enumerate(h):
            if v != heights[idx]:
                ret += 1
        return ret

