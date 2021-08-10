# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.value = 0
        self.helper(root, low, high)
        return self.value

    def helper(self, root, low, high):
        if root:
            self.value += root.val if low <= root.val <= high else 0
            self.helper(root.right, low, high)
            self.helper(root.left, low, high)