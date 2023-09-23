class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

def find_vertex_info(edges, target_value):
    tree = {}
    for parent, child in edges:
        if parent not in tree:
            tree[parent] = TreeNode(parent)
        if child not in tree:
            tree[child] = TreeNode(child)
        tree[child].parent = tree[parent]
        tree[parent].children.append(tree[child])

    def dfs(node, level):
        if node.value == target_value:
            return node.parent, node.children, level
        for child in node.children:
            result = dfs(child, level + 1)
            if result:
                return result

    parent, children, level = dfs(tree[1], 0)
    ancestors = []
    descendants = []

    def find_ancestors(node):
        if node.parent:
            ancestors.append(node.parent.value)
            find_ancestors(node.parent)

    def find_descendants(node):
        for child in node.children:
            descendants.append(child.value)
            find_descendants(child)

    find_ancestors(parent)
    find_descendants(tree[1])
    return parent.value, children, ancestors, descendants, level

# Example usage
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
target_value = 4
result = find_vertex_info(edges, target_value)
print("Parent:", result[0])
print("Children:", result[1])
print("Ancestors:", result[2])
print("Descendants:", result[3])
print("Level:", result[4])
