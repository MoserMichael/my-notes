# 684. Redundant Connection
# Medium
#
#    In this problem, a tree is an undirected graph that is connected and has no cycles.
#
#    You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
#
#    Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
#
#
#
#    Example 1:
#
#    Input: edges = [[1,2],[1,3],[2,3]]
#    Output: [2,3]
#
#    Example 2:
#
#    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
#    Output: [1,4]
#
#
#
#    Constraints:
#
#        n == edges.length
#        3 <= n <= 1000
#        edges[i].length == 2
#        1 <= ai < bi <= edges.length
#        ai != bi
#        There are no repeated edges.
#        The given graph is connected.
#

#
#    Intuition
#
#    an application of union find. the two endpoints are added to the union find structure, if both ends are part of the same set, then we have a cycle.
#    Approach
#
#    union find structure is represented by a map, that maps each element to its set. A set points to its parent set.
#
#    for each link in the set of links:
#
#        if none of the endpoints of a link belong to a set, then form a new set.
#        if both endpoints of a link belong to different sets then form the union of both sets.
#        if both endpoints of a link belong to the same set then report a cycle.
#        if one of the endpoints of a link belong to a set, then add the other endpoint to the same set.
#
#    Complexity
#
#        Time complexity:
#        Something about akkerman functions, but I forgot the lecture.
#        Essentially o(n) as each check does a map lookup to check for which set it belongs to.
#
#

class ASet:
    def __init__(self):
        self.parent = None

    def setParent(aset):
        self.parent = aset


class UnionSet:
    def __init__(self):
        self.members = {}

    def makeSet(self, elm):
        st = ASet()
        self.members[elm] = st
        return st

    def find(self, elm):
        if elm in self.members:
            st = self.members[elm]
            while st.parent is not None:
                st = st.parent
            return st
        return None

    def add(self, st, elm):
        self.members[elm] = st

    def union(self, aset, bset):
        aset.parent = bset



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uset = UnionSet()

        for e in edges:

            a_start = uset.find(e[0])
            a_end = uset.find(e[1])

            if not a_start and not a_end:
                st = uset.makeSet(e[0])
                uset.add(st, e[1])
            elif a_start and a_end:
                if a_start != a_end:
                    uset.union(a_start,a_end)
                else:
                    return e
            else:
                if a_start:
                    uset.add(a_start, e[1])
                else:
                    uset.add(a_end, e[0])






