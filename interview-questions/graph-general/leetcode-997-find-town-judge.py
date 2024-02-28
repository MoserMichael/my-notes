# 997. Find the Town Judge
# Easy
#
#    In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
#
#    If the town judge exists, then:
#
#        The town judge trusts nobody.
#        Everybody (except for the town judge) trusts the town judge.
#        There is exactly one person that satisfies properties 1 and 2.
#
#    You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
#
#    Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
#
#
#
#    Example 1:
#
#    Input: n = 2, trust = [[1,2]]
#    Output: 2
#
#    Example 2:
#
#    Input: n = 3, trust = [[1,3],[2,3]]
#    Output: 3
#
#    Example 3:
#
#    Input: n = 3, trust = [[1,3],[2,3],[3,1]]
#    Output: -1
#
#
#
#    Constraints:
#
#        1 <= n <= 1000
#        0 <= trust.length <= 104
#        trust[i].length == 2
#        All the pairs of trust are unique.
#        ai != bi
#        1 <= ai, bi <= n
#


class Solution:
    def findJudge(self, n_size: int, trust: List[List[int]]) -> int:
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        return Solution.findJudgeFast(n_size, trust)
        #return Solution.findJudgeSlow(n_size, trust)


    # i had to look this one up!
    def findJudgeFast(n, trust):

        trust_me = [0] * n

        for rec in trust:
            src = rec[0]-1
            trg = rec[1]-1
            trust_me[src] -= 1
            trust_me[trg] += 1

        for idx, score in enumerate(trust_me):
            if score == (n-1):
                return idx+1

        return -1 

    def findJudgeSlow(n_size: int, trust: List[List[int]]) -> int:

        graph = Solution.makeArray(n_size, trust)
        
        zero_row = [0] * n_size
        for n in range(n_size):
            if graph[n] == zero_row:
                is_solution = True
                for m in range(n_size):
                    if m != n and graph[m][n] != 1:
                        is_solution = False
                        break
                if is_solution:            
                    return n+1
        return -1
            

    def makeArray(n, trust):
        res = []
        for idx in range(n):
            res.append( [0] * n)
        
        for elm in trust:
            res[elm[0]-1][elm[1]-1] = 1

        return res

       
