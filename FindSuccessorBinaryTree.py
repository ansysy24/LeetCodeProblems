# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    #	1) create traversal list via recursion
    # 	   left -> left -> ... value - right -> value -> right ->...
    # 	2) loop over the list finding the index of the node we look
    #		for num in list: if num == node.value -> return list[i+1]
    tr_list = get_traversal(tree)
    for i, n in enumerate(tr_list):
        if n != node:
            continue
        if i == len(tr_list) - 1:
            return None
        return tr_list[i + 1]


def get_traversal(node, l = []):
    if node.left is not None:
        get_traversal(node.left, l)
    l.append(node)
    if node.right is not None:
        get_traversal(node.right, l)
    return l