# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        return self.helper(root)[1:-1]

    def helper(self, root: TreeNode) -> str:
        if root is None:
            return '()'

        right = self.helper(root.right)
        left = self.helper(root.left)

        right = '' if right == '()' else right
        left = '' if left == '()' and not right else left

        return '(' + str(root.val) + left + right + ')'
