import heapq

class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch          # character
        self.freq = freq      # frequency
        self.left = left      # left child
        self.right = right    # right child

    # for priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq


def build_codes(root, code, huff_map):
    if not root:
        return

    # Leaf node -> store code
    if not root.left and not root.right:
        huff_map[root.ch] = code if code != "" else "0"
        return

    build_codes(root.left, code + "0", huff_map)
    build_codes(root.right, code + "1", huff_map)
def main():
    text = input("Enter text: ")

    # frequency dictionary
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1

    print("\nCharacter Frequencies:")
    for k, v in freq.items():
        print(f"'{k}' : {v}")

    # priority queue (min-heap)
    pq = []
    for char, f in freq.items():
        heapq.heappush(pq, Node(char, f))

    # Build Huffman Tree
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(pq, merged)

    root = heapq.heappop(pq)

    # Generate Huffman codes
    codes = {}
    build_codes(root, "", codes)

    print("\nHuffman Codes:")
    for k, v in codes.items():
        print(f"'{k}' : {v}")

    # Encode input text
    encoded = "".join([codes[ch] for ch in text])

    print("\nEncoded text:", encoded)


if __name__ == "__main__":
    main()
