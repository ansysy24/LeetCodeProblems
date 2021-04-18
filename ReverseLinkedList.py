# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        start = head
        while head.next is not None:
            tmp = head.next
            head.next = head.next.next
            tmp.next = start
            start = tmp

        return start