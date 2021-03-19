def sameBsts(arrayOne, arrayTwo):
    head1 = build_tree(arrayOne) if arrayOne else None
    head2 = build_tree(arrayTwo) if arrayOne else None
    return head1 == head2

def build_tree(array):
    head = Tree(array[0])
    for value in array[1:]:
        head.insert(value)
    return head


class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        if other is None or self.value != other.value:
            return False

        return self.left == other.left and self.right == other.right

    def insert(self, value):
        head = self
        while True:
            if value >= head.value:
                if head.right is None:
                    head.right = Tree(value)
                    break
                head = head.right
            else:
                if head.left is None:
                    head.left = Tree(value)
                    break
                head = head.left


print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]))