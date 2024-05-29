from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1
        elif not list1 and not list2:
            return None
        else:
            start_with_list1 = list1.val <= list2.val
            if start_with_list1:
                merged = ListNode(list1.val)
                list1 = list1.next
            else:
                merged = ListNode(list2.val)
                list2 = list2.next
            root = merged
            while list1 and list2:
                if list1.val <= list2.val:
                    next_node = ListNode(list1.val)
                    merged.next = next_node
                    merged = merged.next
                    list1 = list1.next
                else:
                    next_node = ListNode(list2.val)
                    merged.next = next_node
                    merged = merged.next
                    list2 = list2.next
            if list1:
                while list1:
                    merged.next = list1
                    list1 = list1.next
                    merged = merged.next
            elif list2:
                while list2:
                    merged.next = list2
                    list2 = list2.next
                    merged = merged.next
            return root
