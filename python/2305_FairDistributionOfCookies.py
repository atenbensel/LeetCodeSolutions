# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.
# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.
# Return the minimum unfairness of all distributions.

# Solution:

class Solution(object):
    def distributeCookies(self, cookies, k):
        
        total = [0]*(1<<len(cookies))
        for mask in xrange(1<<len(cookies)):
            total[mask] = sum(cookies[i] for i in xrange(len(cookies)) if mask&(1<<i))
        dp = [[float("inf")]*(1<<len(cookies)) for _ in xrange(2)]
        dp[0][0] = 0
        for i in xrange(k):
            for mask in xrange(1<<len(cookies)):
                submask = mask
                while submask:
                    dp[(i+1)%2][mask] = min(dp[(i+1)%2][mask], max(total[submask], dp[i%2][mask^submask]))
                    submask = (submask-1)&mask
        return dp[k%2][-1]