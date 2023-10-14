# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.next and current.next.val == current.next.next.val:
                duplicate_value = current.next.val
                while current.next and current.next.val == duplicate_value:
                    current.next = current.next.next

            else:
                current = current.next

        return dummy.next
