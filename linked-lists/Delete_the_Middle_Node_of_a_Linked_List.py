from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = head, head
        n = 0
        while h1:
            h1 = h1.next
            n += 1
        mid = n // 2
        if mid != 0:
            counter = 0
            while counter != mid - 1:
                h2 = h2.next
                counter += 1
            tmp = h2
            tmp = tmp.next.next
            h2.next = tmp
            return head
