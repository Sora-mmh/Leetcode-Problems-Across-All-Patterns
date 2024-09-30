from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        left_pointer, right_pointer = head, head
        l_steps, r_steps = 1, 1
        while l_steps != left:
            left_pointer = left_pointer.next
            l_steps += 1
        while r_steps != right:
            right_pointer = right_pointer.next
            r_steps += 1
        after = right_pointer.next
        previous = after
        current = left_pointer
        while current != after:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        if left != 1:
            cursor = ListNode(head.val)
            result = cursor
            head = head.next
            while head != left_pointer:
                cursor.next = ListNode(head.val)
                head = head.next
                cursor = cursor.next
            cursor.next = previous
            return result
        else:
            return previous
