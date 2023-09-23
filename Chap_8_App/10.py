from heapq import heappush, heappop

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def build_huffman_tree(data):
    frequencies = {}
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1

    heap = []
    for char, frequency in frequencies.items():
        heappush(heap, (frequency, HuffmanNode(char, frequency)))

    while len(heap) > 1:
        freq1, node1 = heappop(heap)
        freq2, node2 = heappop(heap)
        combined_node = HuffmanNode(None, freq1 + freq2)
        combined_node.left, combined_node.right = node1, node2
        heappush(heap, (combined_node.frequency, combined_node))

    return heap[0][1]

def huffman_encoding(node, prefix="", code_map={}):
    if node.char:
        code_map[node.char] = prefix
    if node.left:
        huffman_encoding(node.left, prefix + "0", code_map)
    if node.right:
        huffman_encoding(node.right, prefix + "1", code_map)
    return code_map

# Example usage
data = "aabbccc"
root = build_huffman_tree(data)
codes = huffman_encoding(root)
print(codes)
