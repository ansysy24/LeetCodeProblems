"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_dep = 0
        self.helper(root)
        return self.max_dep

    def helper(self, root, level=1):
        if root is None:
            return None

        self.max_dep = max(self.max_dep, level)
        for child in root.children:
            self.helper(child, level + 1)