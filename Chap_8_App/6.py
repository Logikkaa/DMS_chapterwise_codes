class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def find_universal_addresses(edges):
    tree = {}
    for parent, child in edges:
        if parent not in tree:
            tree[parent] = TreeNode(parent)
        if child not in tree:
            tree[child] = TreeNode(child)
        tree[parent].children.append(tree[child])

    addresses = []

    def dfs(node, prefix):
        addresses.append(prefix + [node.value])
        for idx, child in enumerate(node.children):
            dfs(child, prefix + [node.value] + [idx])

    dfs(tree[1], [])
    return addresses

# Example usage
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
addresses = find_universal_addresses(edges)
for address in addresses:
    print(address)
