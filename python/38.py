class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        prev_term = "1"
        
        for _ in range(n - 1):
            curr_term = []
            count = 1
            
            for i in range(1, len(prev_term)):
                if prev_term[i] == prev_term[i - 1]:
                    count += 1
                else:
                    curr_term.append(str(count) + prev_term[i - 1])
                    count = 1
            
            curr_term.append(str(count) + prev_term[-1])
            prev_term = "".join(curr_term)
        
        return prev_term
