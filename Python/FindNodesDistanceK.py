class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dfs(node, parents, target):
    if node.value == target:
        parents['target'] = node
    if node.left is not None:
        parents[node.left.value] = node
        dfs(node.left, parents, target)
    if node.right is not None:
        parents[node.right.value] = node
        dfs(node.right, parents, target)


def findNodesDistanceK(tree, target, k):
    parents = {}
    dfs(tree, parents, target)
    queue = [(parents['target'], 0)]
    current = queue.pop()
    visited = set([current[0]])
    while current[1] != k:
        current_node = current[0]
        if current_node.value in parents and parents[current_node.value] not in visited:
            queue.append((parents[current_node.value], current[1] + 1))
            visited.add(parents[current_node.value])
            del parents[current_node.value]
        if current_node.left is not None and current_node.left not in visited:
            queue.append((current_node.left, current[1] + 1))
            visited.add(current_node.left)
        if current_node.right is not None and current_node.right not in visited:
            queue.append((current_node.right, current[1] + 1))
            visited.add(current_node.right)
        print([(item[0].value, item[1]) for item in queue])
        if queue:
            current = queue.pop(0)
        else:
            return []


    return [item[0].value for item in queue] + [current[0].value]