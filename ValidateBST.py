# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_val=float('-inf'), max_val=float('inf')):
    valid_right = True
    valid_left = True
    if tree.left:
        if min_val <= tree.left.value < tree.value:
            valid_left = validateBst(tree.left, min_val, tree.value)
        else:
            valid_left = False

    if tree.right:
        if max_val > tree.right.value >= tree.value:
            valid_right = validateBst(tree.right, tree.value, max_val)
        else:
            valid_right = False

    return valid_right and valid_left


def validateBst2(tree, min_val=float('-inf'), max_val=float('inf')):
    if tree is None:
        return True

    if tree.value < min_val or tree.value >= max_val:
        return False

    leftIsValid = validateBst(tree.left, min_val, tree.value)

    return leftIsValid and validateBst(tree.right, tree.value, max_val)