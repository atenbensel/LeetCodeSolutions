class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        def ceil(x):
            return int(x) if x == int(x) else int(x) + 1

        if len(dist) >= hour + 1:
            return -1
        
        left, right = 1, ceil(max(max(dist), dist[-1] / (1 if hour.is_integer() else hour - int(hour))))
        
        while left < right:
            mid = (left + right) // 2
            if sum([ceil(i / float(mid)) for i in dist[:-1]]) + (dist[-1] / float(mid)) <= hour:
                right = mid
            else:
                left = mid + 1
        
        return left
