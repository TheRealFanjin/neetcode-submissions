# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        last = head
        count = 0
        while last.next:
            count += 1
            last = last.next
        
        curr = head
        for i in range(int((count) / 2)):
            curr = curr.next
        
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        for i in range(int((count + 1) / 2)):
            temp_head = head.next
            temp_last = last.next
            head.next = last
            last.next = temp_head
            last = temp_last
            head = temp_head