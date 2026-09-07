# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        prev = list2 if list1.val > list2.val else list1
        head = prev
        curr1 = list1.next if prev == list1 else list1
        curr2 = list2.next if prev == list2 else list2

        while curr1 and curr2:
            if curr1.val > curr2.val:
                prev.next = curr2
                curr2 = curr2.next
            else:
                prev.next = curr1
                curr1 = curr1.next
            prev = prev.next
        if curr1:
            prev.next = curr1
        elif curr2:
            prev.next = curr2
        return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        for l in lists:
            res = self.mergeTwoLists(l, res)
        return res
        