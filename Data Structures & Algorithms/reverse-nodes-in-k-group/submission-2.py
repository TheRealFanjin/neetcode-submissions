# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        total_nodes = 0
        curr = head
        while curr:
            total_nodes += 1
            curr = curr.next
        stop_node = total_nodes // k * k
        curr = head
        prev_tail = None
        curr_tail = head
        prev = None
        res = None
        counter = 0
        while counter <= stop_node:
            if counter % k == 0:
                if prev_tail:
                    prev_tail.next = prev
                if not res:
                    res = prev
                prev_tail = curr_tail
                if counter == stop_node:
                    break
                curr_tail = curr
                prev = None
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            counter += 1
        if prev_tail:
            prev_tail.next = curr
        return res
