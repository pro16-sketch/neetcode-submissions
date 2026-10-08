# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val<=list2.val:
            head=list1
            temp1=list1.next
            temp2=list2
        else:
            head = list2
            temp1 = list1
            temp2 = list2.next
        curr = head

        while temp1 is not None and temp2 is not None:

            if temp1.val <= temp2.val:
                curr.next = temp1
                temp1 = temp1.next
            else:
                curr.next = temp2
                temp2 = temp2.next

            curr = curr.next

        if temp1 is not None:
            curr.next = temp1
        else:
            curr.next = temp2

        return head