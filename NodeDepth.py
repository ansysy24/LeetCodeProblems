def nodeDepths(root):
    dsum = []
    helper(root, dsum, 0)
    return sum(dsum)

def helper(root, dsum, csum):
    if root.left is None and root.right is None:
        dsum += [csum]
    else:
        dsum += [csum]
        if root.right is not None:
            helper(root.right, dsum, csum + 1)
        if root.left is not None:
            helper(root.left, dsum, csum + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
