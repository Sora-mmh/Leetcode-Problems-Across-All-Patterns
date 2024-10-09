from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        values = []
        while head:
            values.append(head.val)
            head = head.next
        reversed_values = values[::-1]
        reversed_nodes = [ListNode(val) for val in reversed_values]
        idx = 1
        n = len(reversed_values)
        result = reversed_nodes[0]
        cursor = result
        while idx < n:
            result.next = reversed_nodes[idx]
            result = result.next
            idx += 1
        return cursor
