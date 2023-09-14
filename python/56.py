class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0]) 
        merged = [intervals[0]] 
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_merged_interval = merged[-1]

            if current_interval[0] <= last_merged_interval[1]:
                last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
            else:
                merged.append(current_interval)

        return merged
