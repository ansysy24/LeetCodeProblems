# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    head_copy = head
    leng = 0
    while head_copy is not None:
        leng += 1
        head_copy = head_copy.next

    leng_start = leng - k
    if not leng_start:
        head.value = head.next.value
        head.next = head.next.next
    else:
        prev = None

        while leng_start:
            prev = head
            head = head.next
            leng_start -= 1

        prev.next = head.next
        head.value = 0