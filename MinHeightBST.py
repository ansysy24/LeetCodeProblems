def minHeightBst(array):
    if not array:
        return None
    middle = int(len(array) // 2)

    head = BST(array[middle])
    head.left = minHeightBst(array[:middle])
    head.right = minHeightBst(array[middle + 1:])
    return head


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
