#1743. Restore the Array From Adjacent Pairs
#Medium
#    There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
#
#    You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
#
#    It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
#
#    Return the original array nums. If there are multiple solutions, return any of them.
#
#
#
#    Example 1:
#
#    Input: adjacentPairs = [[2,1],[3,4],[3,2]]
#    Output: [1,2,3,4]
#    Explanation: This array has all its adjacent pairs in adjacentPairs.
#    Notice that adjacentPairs[i] may not be in left-to-right order.
#
#    Example 2:
#
#    Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
#    Output: [-2,4,1,-3]
#    Explanation: There can be negative numbers.
#    Another solution is [-3,1,4,-2], which would also be accepted.
#
#    Example 3:
#
#    Input: adjacentPairs = [[100000,-100000]]
#    Output: [100000,-100000]
#
#
#
#    Constraints:
#
#        nums.length == n
#        adjacentPairs.length == n - 1
#        adjacentPairs[i].length == 2
#        2 <= n <= 105
#        -105 <= nums[i], ui, vi <= 105
#        There exists some nums that has adjacentPairs as its pairs.
#

class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def follow_path(node):
            nonlocal graph
            ret = []

            parent_node = None
            while True:
                #print(f"node: {node} parent_node {parent_node}")
                ret.append(node)
                links = graph[node]
                next_node = None
                for l in links:
                    if parent_node is None or l != parent_node:
                        parent_node = node
                        next_node = l
                        break
                if next_node is None:
                    break
                node = next_node
            return ret

        for p in adjacentPairs:
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])

        #print(graph)
        for k, v in graph.items():
            if len(v) == 1:
                # terminal point.
                return follow_path(k)

        assert False
