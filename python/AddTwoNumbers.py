'''
Question:



Solution:

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.getNumber(l1)
        n2 = self.getNumber(l2)
        return self.addNumber(n1+n2)

    def getNumber(self, ll):
        zero_count = 0
        n = 0
        while ll:
            if ll.val == 0 and n == 0:
                zero_count += 1
            n = n * 10 + ll.val
            ll = ll.next
        return self.reverseNumber(n, zero_count)

    def reverseNumber(self, n, zero_count):
        rn = 0
        while n:
            d = n % 10
            rn = rn * 10 + d
            n //= 10
        return rn * 10 ** zero_count if zero_count else rn

    def addNumber(self, n):
        l = self.countNumberDigits(n)
        i = 0
        digits = [None] * l
        digits[i] = n % 10
        LL = ListNode(digits[i])
        n //= 10
        while n:
            i += 1
            digits[i] = n % 10
            current = LL
            while current.next:
                current = current.next
            current.next = ListNode(n % 10)
            n //= 10
        return LL

    def countNumberDigits(self, n):
        c = 1
        while n // 10:
            c += 1
            n //= 10
        return c