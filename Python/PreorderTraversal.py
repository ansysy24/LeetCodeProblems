from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.lst = []
        self.helper(root)
        return self.lst

    def helper(self, root):
        if root is not None:
            self.lst.append(root.val)

            self.helper(root.left)
            self.helper(root.right)
