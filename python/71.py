class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        components = path.split('/')

        for component in components:
            if component == "..":
                if stack:
                    stack.pop()
            elif component and component != ".":
                stack.append(component)

        return "/" + "/".join(stack)
