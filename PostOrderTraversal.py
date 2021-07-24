# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.traversal = []
        self.helper(root)
        return self.traversal

    def helper(self, root):
        if not root:
            return None

        self.helper(root.left)
        self.helper(root.right)
        self.traversal.append(root.val)