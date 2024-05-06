# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tt = 0

        def tree_sum(root):
            nonlocal tt

            if root == None:
                return 0

            right_sum = tree_sum(root.right)

            left_sum = tree_sum(root.left)

            tt += abs(right_sum - left_sum)

            return root.val + right_sum + left_sum

        tree_sum(root)
        return tt