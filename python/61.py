# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        
        k %= length
        
        if k == 0:
            return head
        
        new_head_index = length - k
        
        current.next = head
        
        current = head
        for _ in range(new_head_index - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        
        return new_head
