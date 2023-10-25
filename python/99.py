# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first_misplaced = [None]
        second_misplaced = [None]
        prev_node = [TreeNode(float('-inf'))]

        def in_order_traversal(node):
            if not node:
                return

            in_order_traversal(node.left)

            if prev_node[0].val > node.val:
                if not first_misplaced[0]:
                    first_misplaced[0] = prev_node[0]
                second_misplaced[0] = node

            prev_node[0] = node

            in_order_traversal(node.right)

        in_order_traversal(root)

        first_misplaced[0].val, second_misplaced[0].val = second_misplaced[0].val, first_misplaced[0].val
