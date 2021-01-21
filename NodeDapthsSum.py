def nodeDepths(root):
	dep = 0
	sum = 0
	level = [root]
	next_level = []
	while level:
		for node in level:
			sum += dep
			if node.right is not None:
				next_level.append(node.right)
			if node.left is not None:
				next_level.append(node.left)
		dep += 1
		level = next_level[:]
		next_level = []
	return sum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None