import heapq
import random
from time import time_ns

class Huffman:
    def __init__(self, symbol=None, frequency=0):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(symbol_frequency):
    heap = [Huffman(symbol, freq) for symbol, freq in symbol_frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        internal_node = Huffman(frequency=left.frequency + right.frequency)
        internal_node.left = left
        internal_node.right = right
        heapq.heappush(heap, internal_node)
    return heap[0]

def generate_huffman_codes(root, current="", code=None):
    if code is None:
        code = {}
    if root is not None:
        if root.symbol is not None:
            code[root.symbol] = current
        generate_huffman_codes(root.left, current + "0", code)
        generate_huffman_codes(root.right, current + "1", code)

def huffman_encoding(symbol_frequency):
    root = build_huffman_tree(symbol_frequency)
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)
    return huffman_codes

input_values = [999,1000,9999,10000,99999,100000,999999,1000000]
for n in input_values:
    symbols = [chr(i) for i in range(n)]
    symbol_frequency = {symbol: random.randint(1, 1000) for symbol in symbols}
    start_time = time_ns()
    huffman_codes = huffman_encoding(symbol_frequency)
    end_time = time_ns()
    Total_time_taken = end_time - start_time
    print(f"\nNumber of Symbols (n): {n}")
    print(f"Time taken: {Total_time_taken} nanoseconds")
