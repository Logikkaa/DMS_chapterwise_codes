class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

def find_vertex_info(tree, target_value):
    def dfs(node, level):
        if node.value == target_value:
            return node.parent, node.children, level
        for child in node.children:
            result = dfs(child, level + 1)
            if result:
                return result

    parent, children, level = dfs(tree, 0)
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
    find_descendants(tree)
    return parent.value, children, ancestors, descendants, level

# Example usage
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6)]

target_value = 5
result = find_vertex_info(root, target_value)
print("Parent:", result[0])
print("Children:", [child.value for child in result[1]])
print("Ancestors:", result[2])
print("Descendants:", result[3])
print("Level:", result[4])
