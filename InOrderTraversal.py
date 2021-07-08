# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.trav = []
        self.helper(root)
        return self.trav

    def helper(self, root):
        if root is None:
            return

        self.helper(root.left)
        self.trav.append(root.val)
        self.helper(root.right)