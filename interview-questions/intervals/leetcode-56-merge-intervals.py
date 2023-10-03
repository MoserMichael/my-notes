#56. Merge Intervals
#Medium
#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#
#
#Example 1:
#
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
#Example 2:
#
#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
#Constraints:
#
#    1 <= intervals.length <= 104
#    intervals[i].length == 2
#    0 <= starti <= endi <= 104
#
#


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return Solution.mergeInterals(intervals)

    @staticmethod
    def mergeInterals(intervals):
        arrayWithMidpoint = []
        for idx in range(0, len(intervals)):
            interv = intervals[idx].copy()
            interv.append(idx)
            interv.append((interv[0]+interv[1])/2)
            arrayWithMidpoint.append(interv)

        arrayWithMidpoint = sorted(arrayWithMidpoint, key = lambda entry : entry[3])

        idx = 0
        while idx < len(arrayWithMidpoint):

            prevIdx = idx-1
            if prevIdx >=0 and Solution.intervalOverlap( arrayWithMidpoint[idx], arrayWithMidpoint[prevIdx] ):

                v1 = arrayWithMidpoint[idx]
                v2 = arrayWithMidpoint[prevIdx]

                mergedInterval = Solution.mergeInterval(v1, v2)

                intervals[ v2[2] ] = mergedInterval
                intervals[ v1[2] ] = None

                arrayWithMidpoint[prevIdx][1] = mergedInterval[1]
                arrayWithMidpoint[prevIdx][0] = mergedInterval[0]
                arrayWithMidpoint.pop(idx)
                idx -= 1
                continue

            nextIdx = idx+1
            if nextIdx < len(arrayWithMidpoint) and Solution.intervalOverlap( arrayWithMidpoint[idx], arrayWithMidpoint[nextIdx] ):

                v1 = arrayWithMidpoint[idx]
                v2 = arrayWithMidpoint[nextIdx]

                mergedInterval = Solution.mergeInterval(v1, v2)

                intervals[ v1[2] ] = mergedInterval
                intervals[ v2[2] ] = None

                arrayWithMidpoint[idx][0] = mergedInterval[0]
                arrayWithMidpoint[idx][1] = mergedInterval[1]
                arrayWithMidpoint.pop(nextIdx)
            else:
                idx = idx + 1

        return filter( lambda elm : elm is not None, intervals)



    @staticmethod
    def mergeInterval(v1, v2):
        return [ min(v1[0], v2[0]), max(v1[1], v2[1]) ]


    #[1,4][1,5] do intersect
    @staticmethod
    def intervalOverlap(v1, v2):
        #ret = not (v1[1] < v2[0] or v2[1] < v1[0])
        ret = v1[1] >= v2[0] and v2[1] >= v1[0]
        return ret








