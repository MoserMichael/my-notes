

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countMap = Solution.count(s)
        minSteps = 0
        for ch in t:
            if ch in countMap:
                if countMap[ch] > 0:
                    countMap[ch] -= 1
                    continue

            minSteps += 1

        return minSteps


    def count(s):
        ret = {}
        for ch in s:
            ret[ch] = ret.setdefault(ch, 0) + 1
        return ret


