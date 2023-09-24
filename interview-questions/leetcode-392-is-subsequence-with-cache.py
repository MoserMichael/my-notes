

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cache = {}
        return Solution.impCache(s, 0, t, 0, cache)

    @staticmethod
    def impCache(s, pos_s, t, pos_t, cache):
        key = f"{pos_s}-{pos_t}"
        if key in cache:
            return cache[key]
        r = Solution.imp(s, pos_s, t, pos_t, cache)
        cache[key] = r
        return r

    @staticmethod
    def imp(s, pos_s, t, pos_t, cache):
        if pos_s == len(s):
            return True
        if pos_t == len(t):
            return False 
        
        if s[pos_s] == t[pos_t]:
            return Solution.impCache(s, pos_s+1, t, pos_t+1, cache)
        
        return Solution.impCache(s, pos_s, t, pos_t+1, cache)

        
