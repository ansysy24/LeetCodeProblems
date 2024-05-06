# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.counter = 0
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return None

        self.helper(root.right)

        self.counter += root.val
        root.val = self.counter

        self.helper(root.left)

        return root