# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        q = l2
        dummy = ListNode(0)
        curr = dummy
        c = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            s = x + y + c
            curr.next = ListNode(s % 10)
            c = s // 10
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if c > 0:
            curr.next = ListNode(c)

        return dummy.next