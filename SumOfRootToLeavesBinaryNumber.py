# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.result = 0

        self.helper(root)
        return self.result

    def helper(self, root, current=''):
        current_bin = current + str(root.val)
        if not root.left and not root.right:
            self.result += int(current_bin, 2)

        if root.left:
            self.helper(root.left, current_bin)
        if root.right:
            self.helper(root.right, current_bin)