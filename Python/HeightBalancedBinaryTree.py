# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    tree_info = helper(tree)
    return tree_info[0]


def helper(tree):
    if tree is None:
        return True, 0

    left = helper(tree.left)
    right = helper(tree.right)

    is_balanced_here = abs(left[1] - right[1]) <= 1
    is_balanced = is_balanced_here and left[0] and right[0]
    leng = max(left[1], right[1]) + 1

    return is_balanced, leng
