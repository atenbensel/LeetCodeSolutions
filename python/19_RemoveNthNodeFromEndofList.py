# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        node = dummy
        for _ in range(length - n):
            node = node.next

        node.next = node.next.next

        return dummy.next
