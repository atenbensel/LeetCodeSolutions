# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        len = 0
        while head:
            len += 1
            head = head.next
        return len

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        len = self.length(head)

        if len < k:
            return head

        cnt = 0
        curr = head
        prev = None
        forward = None

        while curr and cnt < k:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            cnt += 1

        if forward:
            head.next = self.reverseKGroup(forward, k)
            
        return prev
