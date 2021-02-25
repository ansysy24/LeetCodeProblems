# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len1 = 0
        head1 = headA
        while head1:
            len1 += 1
            head1 = head1.next

        len2 = 0
        head2 = headB
        while head2:
            len2 += 1
            head2 = head2.next

        if len1 > len2:
            headA, headB = headB, headA

        diff = abs(len1 - len2)
        while diff:
            headB = headB.next
            diff -= 1

        while id(headB) != id(headA):
            headB = headB.next
            headA = headA.next

        return headA