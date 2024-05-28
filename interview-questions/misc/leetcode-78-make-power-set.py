# 78. Subsets
# Medium
#
#    Given an integer array nums of unique elements, return all possible
#    subsets
#    (the power set).
#
#    The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#
#    Example 1:
#
#    Input: nums = [1,2,3]
#    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#    Example 2:
#
#    Input: nums = [0]
#    Output: [[],[0]]
#
#
#
#    Constraints:
#
#        1 <= nums.length <= 10
#        -10 <= nums[i] <= 10
#        All the numbers of nums are unique.
#
#


#
#    python3 - two non recursive solutions, bitmap and generate all combinations
#
#    Intuition
#
#    Bitmap based ```Solution.bitmap(nums)```
#
#    Take all binary numbers with n bits. Any given number stands for a possible member of the power set (the set of all sets). Now look at the bit representation of that number, bit with position m is either 0 or 1 - this decides if ```nums[m]``` is present in its set or not.
#
#    ```for n in range(2 ** len(nums)):``` - n is in the range between zero and two to the power of n.
#
#    ```cur_set = set()```  - that's the set that is represented by the value of n
#
#    The next loop generates the set where the nth bit decides if a given element is included or not
#    ```
#    idx = 0
#    while n > 0:
#        if n & 1:
#            cur_set.add(nums[idx])
#        n >>= 1
#        idx += 1
#    ret.append(cur_set)
#    ```
#
#    Add the resulting set to the list of results:
#    ```
#    ret.append(cur_set)
#    ```
#    Generate all combinations directly ```Solution.nonRec(nums)```
#
#    start with the empty set ```ret=[ (set(), -1) ], generate and add all sets with one element, then add all sets with two elements, etc.
#
#    Maintain the position of the last range of sets with n elemnts (start and end)
#    Now each elemnt needs to have a tuple of the element set and the index of the last element in the set (for empty set set -1)
#    Reason: when extending a set of two elements to three elements then we need to add all entries with index larger than the last one, otherwise you get repetitions.
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return Solution.bitmap(nums)
        #return Solution.nonRec(nums)

    def bitmap(nums):
        ret = []

        for n in range(2 ** len(nums)):
            cur_set = set()

            idx = 0
            while n > 0:
                if n & 1:
                    cur_set.add(nums[idx])
                n >>= 1
                idx += 1
            ret.append(cur_set)

        return ret

    def nonRec(nums):
        ret = [ (set(), -1) ]
        start = 0
        end = 1

        def add_level(num_elems):
            nonlocal start, end, ret, nums

            for idx in range(start, end):
                s = ret[idx]
                set_entry = s[0]
                max_val = s[1]

                for i in range(s[1]+1, len(nums)):
                    elm = nums[i]
                    if elm not in set_entry:
                        next_s = set_entry.copy()
                        next_s.add(elm)

                        to_add = ( next_s, max(max_val, i) )
                        ret.append( to_add )

            start = end
            end = len(ret)

        for n in range(0, len(nums)):
            add_level(n+1)

        return map(lambda x : list(x[0]), ret)


