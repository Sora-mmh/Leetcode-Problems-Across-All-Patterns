from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cursor = head
        values = []
        while cursor:
            values.append(cursor.val)
            cursor = cursor.next
        n = len(values)
        twin_sums = [values[idx] + values[n - 1 - idx] for idx in range(n)]
        return max(twin_sums)
