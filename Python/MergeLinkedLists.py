# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    if headOne is None:
        return headTwo
    if headTwo is None:
        return headOne

    head_one = headOne
    head_two = headTwo

    if headOne.value <= headTwo.value:
        current = head_one
        other = head_two
    else:
        current = head_two
        other = head_one

    main = current

    while current.next is not None:
        if current.value > other.value:
            current, other = other, current

        if current.next.value > other.value:
            temp = current.next
            current.next = other
            other = temp

        current = current.next

    current.next = other

    return main