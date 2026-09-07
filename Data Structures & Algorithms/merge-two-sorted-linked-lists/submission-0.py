# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            head = list1 if list1.val < list2.val else list2
            prev = list1 if list1.val < list2.val else list2
            curr1, curr2 = list1 if prev != list1 else list1.next, list2 if prev != list2 else list2.next
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    prev.next = curr1
                    prev = curr1
                    curr1 = curr1.next
                else:
                    prev.next = curr2
                    prev = curr2
                    curr2 = curr2.next
            if curr1:
                prev.next = curr1
            elif curr2:
                prev.next = curr2
        elif list1:
            return list1
        elif list2:
            return list2
        else:
            return None
        return head
        