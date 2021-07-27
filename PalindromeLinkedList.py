# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        while len(lst) > 1 and lst[0] == lst[-1]:
            lst.pop(0)
            lst.pop()
        return len(lst) < 2
