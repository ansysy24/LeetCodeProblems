def inOrderTraverse(tree, array):
    helper1(tree, array)
    return array


def helper1(tree, array):
    if tree.left is not None:
        helper1(tree.left, array)
    array.append(tree.value)
    if tree.right is not None:
        helper1(tree.right, array)


def preOrderTraverse(tree, array):
    helper2(tree, array)
    return array


def helper2(tree, array):
    array.append(tree.value)
    if tree.left is not None:
        helper2(tree.left, array)
    if tree.right is not None:
        helper2(tree.right, array)


def postOrderTraverse(tree, array):
    helper3(tree, array)
    return array


def helper3(tree, array):
    if tree.left is not None:
        helper3(tree.left, array)
    if tree.right is not None:
        helper3(tree.right, array)
    array.append(tree.value)
