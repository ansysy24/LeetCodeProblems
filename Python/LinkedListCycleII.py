# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return None

        first = head.next
        second = head.next.next

        while first and second and first.next and second.next and second.next.next and first != second:
            first = first.next
            second = second.next.next

        if not first or not second or not first.next or not second.next or not second.next.next:
            return None

        first = head

        while first != second:
            first = first.next
            second = second.next

        return first