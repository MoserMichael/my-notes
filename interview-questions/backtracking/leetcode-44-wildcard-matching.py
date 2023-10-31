# 44. Wildcard Matching
# Hard
#    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#
#        '?' Matches any single character.
#        '*' Matches any sequence of characters (including the empty sequence).
#
#    The matching should cover the entire input string (not partial).
#
#
#
#    Example 1:
#
#    Input: s = "aa", p = "a"
#    Output: false
#    Explanation: "a" does not match the entire string "aa".
#
#    Example 2:
#
#    Input: s = "aa", p = "*"
#    Output: true
#    Explanation: '*' matches any sequence.
#
#    Example 3:
#
#    Input: s = "cb", p = "?a"
#    Output: false
#    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#
#
#
#    Constraints:
#
#        0 <= s.length, p.length <= 2000
#        s contains only lowercase English letters.
#        p contains only lowercase English letters, '?' or '*'.
#


#    # Intuition
#    First approach was to match the regex while parsing it, but that was too slow. The regular expression needs to be optimized. things like ```a****b``` need to be rewritten as ```a*b```.  Also match like ```*aaaaa``` - here the string part of ```aaaaa``` should not be matched recursively letter by letter 0, you need to search for the string ```aaaaa```.
#
#    # Approach
#
#    - Compile the regular expression into an array of ```Entry``` records. Now ```Entry.STR``` matches a string sequence. A ```*``` is translated into an ```Entry.WILDCARD``` record, this one has the ```next``` reference to the next record - if the next record is a string, then search for an exact match. If no match for this string is found, then stop with failure.
#    - Greedy matching: a sequence of ```Entry.WILDCARD``` and ```Entry.ANY``` does not lead ot recursive call, only a wildcard record does that.
#
#    # Complexity
#    - Time complexity: In the worst case each wildcard match would add another power of n, but there are optimizations to exclude this worst case.
#
#    <!-- Add your time complexity here, e.g. $$O(n)$$ -->
#
#    - Space complexity:
#    <!-- Add your space complexity here, e.g. $$O(n)$$ -->
#

import re


class Entry:
    WILDCARD=1
    ANYCHAR=2
    STR=3

    def __init__(self, ty, val = None):
        self.ty = ty
        self.val = val
        self.next = None

    def __repr__(self):
        return f"(ty: {self.ty} val: {self.val} next: {self.next})"


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pat = Solution.compilePattern(p)
        try:
            return Solution.doMatch(pat, 0, s, 0)
        except:
            return False

    def doMatch(pat, pat_idx, s, s_idx):


        idx = s_idx
        while True:
            if idx == len(s):
                if pat_idx == len(pat):
                    return True
                if pat[pat_idx].ty == Entry.WILDCARD and pat[pat_idx].next is None:
                    return True
                return False

            if pat_idx == len(pat):
                return False

            pval = pat[pat_idx]
            pat_idx += 1

            if pval.ty == Entry.STR:
                if s[idx:(idx+len(pval.val))] == pval.val:
                    idx += len(pval.val)
                else:
                    return False
            elif pval.ty == Entry.ANYCHAR:
                if len(s) - idx >= pval.val:
                    idx += pval.val
                else:
                    return False
            else: # wildchar!
                if not pval.next:
                    return True
                if pval.next.ty == Entry.ANYCHAR:
                    idx += pval.next.val
                    while idx <= len(s):
                        if Solution.doMatch(pat, pat_idx+1, s, idx):
                            return True
                        idx+=1

                    return False
                elif pval.next.ty == Entry.STR:
                    match_count = 0
                    while True:
                        r = s.find(pval.next.val,idx)
                        if r != -1:
                            match_count += 1
                            idx = r
                            if Solution.doMatch(pat, pat_idx+1, s, idx + len(pval.next.val)):
                                return True
                            idx += 1
                        else:
                            break
                    if not match_count:
                        raise Exception()
                    return False





    def compilePattern(p):
        ret = []
        idx = 0
        for idx in range(0, len(p)):
            if p[idx] == '*':
                if len(ret) != 0 and ret[-1].ty == Entry.WILDCARD:
                    continue
                ret.append(Entry(Entry.WILDCARD))
            elif p[idx] == '?':
                if len(ret) != 0 and ret[-1].ty == Entry.ANYCHAR:
                    ret[-1].val += 1
                else:
                    ret.append(Entry(Entry.ANYCHAR, 1))
            else:
                if len(ret) != 0 and ret[-1].ty == Entry.STR:
                    ret[-1].val += p[idx]
                else:
                    ret.append(Entry(Entry.STR,p[idx]))

            if len(ret) > 1 and ret[-2].ty == Entry.WILDCARD:
                ret[-2].next = ret[-1]

        return ret



