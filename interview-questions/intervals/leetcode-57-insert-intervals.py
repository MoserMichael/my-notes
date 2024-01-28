# 57. Insert Interval
# Medium
#    You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
#    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
#    Return intervals after the insertion.
#
#
#
#    Example 1:
#
#    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#    Output: [[1,5],[6,9]]
#
#    Example 2:
#
#    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#    Output: [[1,2],[3,10],[12,16]]
#    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
#
#    Constraints:
#
#        0 <= intervals.length <= 104
#        intervals[i].length == 2
#        0 <= starti <= endi <= 105
#        intervals is sorted by starti in ascending order.
#        newInterval.length == 2
#        0 <= start <= end <= 105
#




class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        added = False
        for idx in range(len(intervals)):

            if  newInterval[0] < intervals[idx][0]:
                intervals.insert(idx, newInterval)
                added = True
                break

            if Solution.is_overlap(newInterval, intervals[idx]):
                #assert intervals[idx][0] <= newInterval[0]
                intervals[idx][1] = max(intervals[idx][1],newInterval[1])
                added = True
                break


        if not added:
            intervals.append(newInterval)
            return intervals


        # compare if overlap with any remaining
        cidx = idx + 1

        while cidx < len(intervals):
            if intervals[idx][1] < intervals[cidx][0]:
                break

            if Solution.is_overlap(intervals[idx], intervals[cidx]):
                #assert intervals[idx][0] <= intervals[cidx][0]
                intervals[idx][1] = max(intervals[idx][1], intervals[cidx][1])
                intervals.pop(cidx)
            else:
                cidx += 1
        return intervals

    def is_overlap(int1, int2): #  x1,x2,y1,y2):
        return max(int1[0],int2[0]) <= min(int1[1], int2[1])
        #return max(x1,y1) <= min(x2,y2)
