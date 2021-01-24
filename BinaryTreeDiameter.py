class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    left = helper(tree.left)
    right = helper(tree.right)
    return max(left + right, getattr(tree.left, 'mx', 0), getattr(tree.right, 'mx', 0))


def helper(tree):
    if tree is None:
        return 0

    if tree.left is None and tree.right is None:
        tree.mx = 0

    left = helper(tree.left)
    right = helper(tree.right)
    tree.mx = max(left + right, getattr(tree.left, 'mx', 0), getattr(tree.right, 'mx', 0))
    return max(left, right) + 1