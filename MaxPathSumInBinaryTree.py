def maxPathSum(tree):
    max_path_left, max_half_left = helper(tree.left)
    max_path_right, max_half_right = helper(tree.right)

    max_path = max(max_path_left, max_path_right, max_half_left + max_half_right + tree.value,
                   max_half_right + tree.value, max_half_left + tree.value)

    return max_path


def helper(tree):
    if tree is None:
        return float('-Inf'), 0

    max_path_left, max_half_left = helper(tree.left)
    max_path_right, max_half_right = helper(tree.right)

    max_path = max(max_path_left, max_path_right, max_half_left + max_half_right + tree.value,
                   max_half_right + tree.value, max_half_left + tree.value)
    max_half = max(max_half_left, max_half_right) + tree.value

    return max_path, max_half