# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    if head is None or head.next is None:
        return head

    main = head
    swap = head.next
    new = swap.next
    while swap is not None:
        new = swap.next
        swap.next = head
        main.next = new
        head = swap
        swap = main.next

    return head