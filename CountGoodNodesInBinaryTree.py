# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0
        self.helper(root, float('-inf'))
        return self.counter

    def helper(self, root, curr_max):
        if not root: return

        if root.val >= curr_max:
            curr_max = root.val
            self.counter += 1

        self.helper(root.left, curr_max)
        self.helper(root.right, curr_max)