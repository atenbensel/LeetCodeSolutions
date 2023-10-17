# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        next_node = None

        for _ in range(right - left + 1):
            next_temp = current.next
            current.next = next_node
            next_node = current
            current = next_temp

        prev.next.next = current
        prev.next = next_node

        return dummy.next
