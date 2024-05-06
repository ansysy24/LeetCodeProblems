class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(values):
    head = BST(values.pop(0))
    while values:
        nxt = values.pop(0)
        insert_value_into_tree(head, nxt)
    return head

def insert_value_into_tree(head, value):
    while True:
        if value >= head.value:
            if head.right is None:
                head.right = BST(value)
                break
            head = head.right
        else:
            if head.left is None:
                head.left = BST(value)
                break
            head = head.left

print(reconstructBst([10, 4, 2, 1, 5, 17, 19, 18]))