# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.leafs = []
        self.helper(root1)
        leafs2 = self.leafs.copy()
        self.leafs = []
        self.helper(root2)
        return self.leafs == leafs2

    def helper(self, root):
        if not root.left and not root.right:
            self.leafs.append(root.val)
            return
        if root.left:
            self.helper(root.left)
        if root.right:
            self.helper(root.right)