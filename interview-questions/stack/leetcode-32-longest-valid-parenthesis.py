# 32. Longest Valid Parentheses
# Hard
#Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
#substring
#.
#
#
#
#Example 1:
#
#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".
#
#Example 2:
#
#Input: s = ")()())"
#Output: 4
#Explanation: The longest valid parentheses substring is "()()".
#
#Example 3:
#
#Input: s = ""
#Output: 0
#
#
#
#Constraints:
#
#    0 <= s.length <= 3 * 104
#    s[i] is '(', or ')'.


# solution in one pass: (slow and inefficient)

# From starting position: validate the expression by maintaining a counter of open brackets. Pass over the input from left to right.
# - increment counter upon '('
# - decremet counter upon ')'
# If counter drops below zero, then expression is not valid; this means skip current position to after the current position.

# problem: last expression that is not closed, like (()()(
# here maintain a stack of entries:
#   - each element contains count of expressions passed at given level of nesting
#   - in example: level 0 - no expressions parsed ; level 1 parsed 4 ()()
# Upon completion:
#   - examine stack of incomplete expressions, return maximum of parsed length

# in most cases it would be faster to solve the last incomplete expression by another pass from right to left (reverse direction), which would stop upon validation of the first complete expression, then take the maximum.
# this way you don't have to maintain that stack, but may have to pass over the input twice (in the worst case)

# it is much more simple to keep a stack of open parenthesis+position, then adjust the max length when the parenthesis closes.
# (my solution is just overcomplicated, to see how to overcomplicate things)

class StackLevel:
    def __init__(self, pos):
        self.len_parsed = 0
        self.start_pos = self.init_pos = pos

    def add_pos(self, pos):
        if self.init_pos == -1:
            self.init_pos = pos
        else:
            if self.start_pos + self.len_parsed == self.init_pos:
                self.len_parsed += pos - self.init_pos + 1
            else:
                self.len_parsed = pos - self.init_pos + 1
                self.start_pos = self.init_pos
            self.init_pos = -1

    def get_len(self):
        return self.len_parsed

    def __repr__(self):
        return f"parsed {self.len_parsed} start: {self.start_pos}"

class Solution:

    def longestValidParentheses(self, s: str) -> int:

        idx = 0
        max_len = 0

        while idx < len(s):
            eof, fail_pos, last_count, count_array = Solution.is_valid(s, idx)
            #print(f"eof: {eof} fail_pos {fail_pos} last_count {last_count} - {repr(count_array)}")

            if not eof:
                if len(count_array) != 0:
                    level = count_array[0]
                    max_len = max(max_len, level.get_len())

            if eof:
                for zidx in range(0, len(count_array)):
                    level = count_array[zidx]
                    max_len = max(max_len, level.get_len())
                break

            if fail_pos != -1:
                idx = fail_pos

        return max_len

    def is_valid(s, pos):
        count_arr = []
        idx = pos
        count = 0
        while idx < len(s):
            do_dec = False

            if s[idx] == '(':
                count += 1
            elif s[idx] == ')':
                do_dec = True

            if count > 0:
                if count > len(count_arr):
                    count_arr.append( StackLevel(idx) )
                else:
                    count_arr[ count-1 ].add_pos(idx)

            if do_dec:
                count -= 1

            if count < 0:
                return False, idx+1, count, count_arr

            idx += 1

        return True, idx, count, count_arr

