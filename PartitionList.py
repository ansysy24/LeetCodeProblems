

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        answer = head
        last_lo = None
        while head and head.val < x:
            last_lo = head
            head = head.next
        temp = None
        temp_lo = None
        while head and head.next:
            print(head.val)
            if head.next.val < x:
                temp = head.next
                head.next = head.next.next

                if last_lo:
                    temp_lo = last_lo.next
                    last_lo.next = temp
                    temp.next = temp_lo
                    last_lo = last_lo.next
                else:
                    temp.next = answer
                    answer = temp
                    last_lo = answer
            else:
                head = head.next

        return answer