# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = float('inf')
        self.result = float('inf')
        self.traverse(root)
        return self.result
    
    def traverse(self, root):
        if root:
            self.traverse(root.left)
            self.result = min(self.result, abs(root.val-self.prev))
            self.prev = root.val
            self.traverse(root.right)