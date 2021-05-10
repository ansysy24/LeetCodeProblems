# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sums = []
        self.helper(root, 1)
        return self.sums[-1]

    def helper(self, root, level):

        if root is None:
            return None

        if len(self.sums) < level:
            self.sums.append(root.val)
        else:
            self.sums[level - 1] += root.val

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)