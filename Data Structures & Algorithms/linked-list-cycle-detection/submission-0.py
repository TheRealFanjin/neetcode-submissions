# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        curr = head
        while curr:
            if curr in node_set:
                return True
            node_set.add(curr)
            curr = curr.next
        return False