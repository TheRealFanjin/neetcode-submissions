# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        curr_res = head
        carry = l1.val + l2.val >= 10
        curr_l1 = l1.next
        curr_l2 = l2.next
        while curr_l1 and curr_l2:
            if carry:
                curr_res.next = ListNode((curr_l1.val + curr_l2.val + 1) % 10)
            else:
                curr_res.next = ListNode((curr_l1.val + curr_l2.val) % 10)
            carry = curr_l1.val + curr_l2.val >= 10
            curr_res = curr_res.next
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
        remaining = curr_l1 if curr_l1 else curr_l2
        while remaining:
            if carry:
                curr_res.next = ListNode((remaining.val + 1) % 10)
                carry = remaining.val + 1 >= 10
            else:
                curr_res.next = ListNode(remaining.val)
            curr_res = curr_res.next
            remaining = remaining.next
        if carry:
            curr_res.next = ListNode(1)
        return head



