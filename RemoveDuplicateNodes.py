class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    start = linkedList
    while linkedList.next is not None:
        if linkedList.value == linkedList.next.value:
            linkedList.next = linkedList.next.next
        else:
            linkedList = linkedList.next
    return start
