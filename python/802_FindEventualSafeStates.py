class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        visited = [0] * n
        result = []

        def isSafe(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False

            visited[node] = 2

            for neighbor in graph[node]:
                if not isSafe(neighbor):
                    return False

            visited[node] = 1
            return True

        for i in range(n):
            if isSafe(i):
                result.append(i)

        return result
