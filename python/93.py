class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for step in range(1, 4):
                if start + step <= len(s):
                    segment = s[start:start+step]
                    if 0 <= int(segment) <= 255 and (segment == "0" or segment[0] != "0"):
                        backtrack(start + step, path + [segment])
        
        result = []
        if len(s) >= 4 and len(s) <= 12:
            backtrack(0, [])
        return result
