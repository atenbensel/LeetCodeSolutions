class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for course, pre in prerequisites:
            graph[course].append(pre)

        def isCyclic(node):
            if visited[node] == -1:
                return True
            if visited[node] == 1:
                return False

            visited[node] = -1

            for pre in graph[node]:
                if isCyclic(pre):
                    return True

            visited[node] = 1
            return False

        for course in range(numCourses):
            if isCyclic(course):
                return False

        return True
