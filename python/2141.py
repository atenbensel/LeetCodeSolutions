class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        def can_run_all_computers(run_time):
            count = 0
            for battery in batteries:
                count += min(battery, run_time)
                if count >= n * run_time:
                    return True
            return False

        left, right = 1, sum(batteries)

        while left < right:
            mid = (left + right + 1) // 2
            if can_run_all_computers(mid):
                left = mid
            else:
                right = mid - 1

        return left
