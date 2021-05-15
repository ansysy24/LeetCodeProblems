# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.counter = 0
        self.helper(root)
        return self.counter

    def helper(self, root: TreeNode) -> int:
        l1, l2, r1, r2 = 0, 0, 0, 0
        if root.left:
            self.helper(root.left)
            if root.left.left:
                l1 = root.left.left.val

            if root.left.right:
                l2 = root.left.right.val

        if root.right:
            self.helper(root.right)
            if root.right.left:
                r1 = root.right.left.val

            if root.right.right:
                r2 = root.right.right.val

        if root.val % 2 == 0:
            self.counter += r1 + r2 + l1 + l2