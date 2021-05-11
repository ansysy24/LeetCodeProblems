# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        return self.helper(root, targetSum)

    def helper(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None and targetSum == root.val:
            return True

        return self.helper(root.left, targetSum - root.val) or self.helper(root.right, targetSum - root.val)