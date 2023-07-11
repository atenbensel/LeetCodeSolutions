# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            
            return dummy.next
        
        def mergeLists(lists, start, end):

            if start == end:
                return lists[start]
            
            mid = start + (end - start) // 2
            
            left = mergeLists(lists, start, mid)
            right = mergeLists(lists, mid + 1, end)
            
            return mergeTwoLists(left, right)
        
        return mergeLists(lists, 0, len(lists) - 1)
