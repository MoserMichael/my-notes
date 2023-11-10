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
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #return Solution.count_trust_and_trusted(n, trust)
        return Solution.count_trusted(n, trust) # this one is faster

    def count_trusted(n, trust):

        map_id_to_trust_count = {}

        # that's a second pass to create this one - but it is relatively fast.
        trusts_no_one = set(range(1,n+1))

        candidate = -1
        for t in trust:
            if t[0] in trusts_no_one:
                trusts_no_one.remove(t[0])
            #trusts_no_one.discard(t[0])

            tcount = map_id_to_trust_count.setdefault(t[1], 0) + 1
            map_id_to_trust_count[t[1]] = tcount
            if tcount == n - 1:
                candidate = t[1]

        if len(trusts_no_one) != 1:
            return -1
        if len(map_id_to_trust_count) == 0:
            return 1
        return candidate


    def count_trust_and_trusted(n, trust):
        if n == 1 and len(trust) == 0:
            return 1
        map_id_to_person = {}

        for t in trust:
            from_p = map_id_to_person.setdefault( t[0], [0, 0])
            to_p = map_id_to_person.setdefault( t[1], [0, 0])

            from_p[0] += 1 # trusts a persons
            to_p[1] += 1 # is being trusted by a person

        to_trust = n - 1
        for k, entry in map_id_to_person.items():
            if entry[0] == 0 and  entry[1] == to_trust:
                return k

        return -1



