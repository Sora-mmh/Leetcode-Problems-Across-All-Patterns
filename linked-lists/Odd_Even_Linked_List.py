from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        else:
            n = 1
            right = head
            while right.next:
                right = right.next
                n += 1
            left = head.next
            de = head
            remain = n // 2
            while remain != 0:
                even_node = ListNode(left.val)
                right.next = even_node
                right = right.next
                de.next = left.next
                de = de.next
                left = left.next.next
                remain -= 1
            return head
