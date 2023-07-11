# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        result = []
        parent = {}

        def buildParent(node, par=None):
            if node:
                parent[node] = par
                buildParent(node.left, node)
                buildParent(node.right, node)

        buildParent(root)

        def bfs(node):
            queue = collections.deque([(node, 0)])

            visited = set([node])

            while queue:
                curr, distance = queue.popleft()

                if distance == k:
                    result.append(curr.val)

                for neighbor in [curr.left, curr.right, parent[curr]]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))

        bfs(target)
        return result
