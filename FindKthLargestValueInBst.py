class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, value, counter):
        self.value = value
        self.counter = counter


def findKthLargestValueInBst(tree, k):
    tree_info = TreeInfo(-1, 0)
    helper(tree, k, tree_info)
    return tree_info.value


def helper(tree, k, tree_info):
    if tree is None:
        return

    helper(tree.right, k, tree_info)
    if tree_info.counter == k:
        return
    else:
        tree_info.value = tree.value
        tree_info.counter += 1
        helper(tree.left, k, tree_info)
