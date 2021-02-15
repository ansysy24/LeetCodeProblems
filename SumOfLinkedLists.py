class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(l1, l2):
    current_value = l1.value + l2.value
    transfer = 0 if current_value < 10 else 1
    current_value = current_value % 10
    l1 = l1.next
    l2 = l2.next
    l3 = LinkedList(current_value)
    l4 = l3
    while l1 is not None or l2 is not None:
        current_value = transfer
        if l1 is not None:
            current_value += l1.value
            l1 = l1.next
        if l2 is not None:
            current_value += l2.value
            l2 = l2.next
        transfer = 0 if current_value < 10 else 1
        current_value = current_value%10
        l3.next = LinkedList(current_value)
        l3 = l3.next
    if transfer:
        l3.next = LinkedList(1)
    return l4
