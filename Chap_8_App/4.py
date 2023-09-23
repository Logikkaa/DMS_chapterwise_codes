class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def construct_binary_search_tree(items):
    root = None
    for item in items:
        root = insert(root, item)
    return root

# Example usage
items = [5, 3, 8, 2, 4, 7, 9]
root = construct_binary_search_tree(items)
