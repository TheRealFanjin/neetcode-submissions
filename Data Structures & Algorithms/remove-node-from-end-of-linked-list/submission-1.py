# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1_counter = -n + 1
        p1, p2 = head, head
        while p2.next:
            if p1_counter > 0:
                p1 = p1.next
            else:
                p1_counter += 1
            p2 = p2.next
        if p1_counter == 0 and p1 == head:
            return head.next
        p1.next = p1.next.next
        return head