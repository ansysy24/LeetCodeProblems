# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.steps = 0
        self.helper(root)
        return self.steps

    def helper(self, root):
        if not root:
            return 0

        L = self.helper(root.left)

        R = self.helper(root.right)

        self.steps += abs(L) + abs(R)

        return R + L + root.val - 1