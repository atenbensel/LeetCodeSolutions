class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda x: x[0])
        n = len(events)
        memo = {}

        def dp(idx, k):
            # Base Case 
            if idx == n or k == 0:
                return 0

            if (idx, k) in memo:
                return memo[(idx, k)]

            # Find event that starts after the current event
            next_event_idx = find_next_event(events, idx)

            # Find the value of events by skipping or attending
            memo[(idx, k)] = max(dp(next_event_idx, k - 1) + events[idx][2], dp(idx + 1, k))
            return memo[(idx, k)]

        # Find next event using binary search
        def find_next_event(events, idx):
            end_day = events[idx][1]
            lo, hi = idx + 1, n - 1

            while lo <= hi:
                mid = lo + (hi -lo) // 2
                if events[mid][0] > end_day:
                    hi = mid -1
                else:
                    lo = mid + 1

            return lo

        return dp(0, k)
