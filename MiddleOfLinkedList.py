# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = head
        while head2.next:
            head = head.next
            head2 = head2.next
            if head2.next:
                head2 = head2.next

        return head
