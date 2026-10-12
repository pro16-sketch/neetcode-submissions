# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        t = head
        h = head

        # 1. Find middle
        while h and h.next:
            h = h.next.next
            t = t.next

        # 2. Disconnect second half
        second = t.next
        t.next = None

        # 3. Reverse second half
        prev = None
        cur = second

        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 4. Merge both halves
        first = head
        second = prev

        while second is not None:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        