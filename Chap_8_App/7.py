def preorder_traversal(node):
    if node:
        print(node.value, end=" ")
        for child in node.children:
            preorder_traversal(child)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.children[0])
        print(node.value, end=" ")
        for child in node.children[1:]:
            inorder_traversal(child)

def postorder_traversal(node):
    if node:
        for child in node.children:
            postorder_traversal(child)
        print(node.value, end=" ")

# Example usage
preorder_traversal(tree[1])
print()
inorder_traversal(tree[1])
print()
postorder_traversal(tree[1])
