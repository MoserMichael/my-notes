# 131. Palindrome Partitioning
# Medium
#
#    Given a string s, partition s such that every
#    substring
#    of the partition is a
#    palindrome
#    . Return all possible palindrome partitioning of s.
#
#
#
#    Example 1:
#
#    Input: s = "aab"
#    Output: [["a","a","b"],["aa","b"]]
#
#    Example 2:
#
#    Input: s = "a"
#    Output: [["a"]]
#
#
#
#    Constraints:
#
#        1 <= s.length <= 16
#        s contains only lowercase English letters.
#
#



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ret = []
        self.rec_no_memo(s, 0, [])
        return self.ret


    def rec_no_memo(self, in_str, pos_in_str, partition):
        if pos_in_str == len(in_str):
            self.ret.append(partition.copy())
            return

        for sz in range(0, len(in_str)-pos_in_str):

            eof_pos = pos_in_str+sz+1
            st = in_str[pos_in_str:eof_pos]
            if Solution.isPoly(st):
                partition.append(st)
                self.rec_no_memo(in_str, pos_in_str+sz+1, partition)
                partition.pop()

    def isPoly(str):
        for idx in range(0, len(str)//2):
            if str[idx] != str[-(idx+1)]:
                return False
        return True
