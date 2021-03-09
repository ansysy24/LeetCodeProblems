# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


    def shiftLinkedList(head, k):
        head_copy = head
        leng = 0


        while head is not None:
            leng += 1
            head = head.next

        k = k % leng

        m = leng - k - 1

        head = head_copy

        while m > 0:
            m -= 1
            head = head.next

        main = head.next
        head.next = None

        result = main

        while main and main.next is not None:
            main = main.next

        if main is not None:
            main.next = head_copy

        return result