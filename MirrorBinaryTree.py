def invertBinaryTree(tree):
    if tree is not None:
        tree.right, tree.left = tree.left, tree.right
        invertBinaryTree(tree.right)
        invertBinaryTree(tree.left)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None