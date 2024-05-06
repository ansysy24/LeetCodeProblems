# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def traverse(self, root):
        if root.left is not None:
            self.traverse(root.left)
        self.iterator.append(root)
        if root.right is not None:
            self.traverse(root.right)

    def __init__(self, root: TreeNode):
        self.iterator = []
        self.traverse(root)
        self.i = 0

    def next(self) -> int:
        self.i += 1
        return self.iterator[self.i - 1].val

    def hasNext(self) -> bool:
        if self.i < len(self.iterator):
            return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()