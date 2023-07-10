class Solution:
    def largestVariance(self, s: str) -> int:
        
        def helper(arr):
            n = len(arr)
            dp1 = [0] * n
            dp2 = [0] * n
            dp1[0] = arr[0]
            dp2[-1] = arr[-1]
            
            for i in range(1,n):
                dp1[i] = max(arr[i], dp1[i-1] + arr[i])
            
            for j in range(n-2,-1,-1):
                dp2[j] = max(arr[j], dp2[j+1] + arr[j])
            
            ans = 0
            for k in range(n):
                if arr[k] == -1:
                    ans = max(ans, dp1[k] + dp2[k] - arr[k])
            return ans
        
        res = 0
        lookup = Counter(s)
        for c1 in lookup:
            for c2 in lookup:
                if c1 != c2:
                    arr = []
                    for c in s:
                        if c1 == c:
                            arr.append(1)
                        elif c2 == c:
                            arr.append(-1)
                    res = max(res, helper(arr))
        return res
