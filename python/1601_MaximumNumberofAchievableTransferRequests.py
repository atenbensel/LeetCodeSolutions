# Part of Juleet code 2023
# Question: 1601. Maximum Number of Achievable Transfer Requests
# We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.
# You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer from building fromi to building toi.
# All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.
# Return the maximum number of achievable requests.

# Solution:

class Solution(object):
    def maximumRequests(self, n, requests):
        self.max_requests = 0

        def backtrack(index, curr_requests, net_changes):
            if index == len(requests):
                if all(change == 0 for change in net_changes):
                    self.max_requests = max(self.max_requests, curr_requests)
                return

            fromi, toi = requests[index]
            net_changes[fromi] -= 1
            net_changes[toi] += 1
            backtrack(index + 1, curr_requests + 1, net_changes)

            net_changes[fromi] += 1
            net_changes[toi] -= 1
            backtrack(index + 1, curr_requests, net_changes)

        net_changes = [0] * n
        backtrack(0, 0, net_changes)

        return self.max_requests

