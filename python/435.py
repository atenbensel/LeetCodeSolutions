class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        count, end = 1, intervals[0][1]
        
        for start, e in intervals[1:]:
            if start >= end:
                count += 1
                end = e
        
        return len(intervals) - count
