# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def values_list_left(self, node):
        if node is not None:
            self.values_list_left(node.left)
            self.values_left.append('r')
            self.values_left.append(node.val)
            self.values_list_left(node.right)
            self.values_left.append('l')

    def values_list_right(self, node):
        if node is not None:
            self.values_list_right(node.right)
            self.values_right.append('r')
            self.values_right.append(node.val)
            self.values_list_right(node.left)
            self.values_right.append('l')

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left:
            return root.right is None
        elif not root.right:
            return root.left is None

        self.values_left = []
        self.values_right = []
        self.values_list_left(root.left)
        self.values_list_right(root.right)
        return self.values_left == self.values_right