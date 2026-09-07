# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if not fast.next:
            mid = slow
        else:
            mid = slow.next
        
        curr = mid
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        f_curr = head
        b_curr = prev
        prev = ListNode()
        while f_curr != mid:
            prev.next = f_curr
            temp = f_curr.next
            f_curr.next = b_curr
            prev = b_curr
            b_curr = b_curr.next
            f_curr = temp
        
        if b_curr:
            prev.next = b_curr
