# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = False
        res = None
        rescurr = None
        while curr1 and curr2:
            if carry:
                val = curr1.val + curr2.val + 1
            else:
                val = curr1.val + curr2.val
            if val >= 10:
                n = ListNode(val - 10)
                carry = True
            else:
                n = ListNode(val)
                carry = False
            if not res:
                res = n
                rescurr = n
            else:
                rescurr.next = n
                rescurr = rescurr.next
            curr1 = curr1.next
            curr2 = curr2.next
        if curr1:
            extra = curr1
        else:
            extra = curr2
        while extra:
            if carry:
                val = extra.val + 1
            else:
                val = extra.val
            if val >= 10:
                rescurr.next = ListNode(val - 10)
                carry = True
            else:
                rescurr.next = ListNode(val)
                carry = False
            extra = extra.next
            rescurr = rescurr.next
        if carry:
            rescurr.next = ListNode(1)
        return res