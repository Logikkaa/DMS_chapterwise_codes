def locate_or_add(root, value):
    if root is None:
        return TreeNode(value)
    if value == root.value:
        return root
    if value < root.value:
        root.left = locate_or_add(root.left, value)
    else:
        root.right = locate_or_add(root.right, value)
    return root

# Example usage
root = locate_or_add(root, 6)
