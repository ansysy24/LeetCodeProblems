"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        result = []
        cur_level = [root]
        while cur_level:
            next_level = []
            cur_level_vals = []
            for node in cur_level:
                next_level += node.children
                cur_level_vals.append(node.val)

            result.append(cur_level_vals)
            cur_level = next_level

        return result