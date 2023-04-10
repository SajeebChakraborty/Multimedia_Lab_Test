from heapq import heappush, heappop
from collections import Counter

class Node:
    #constructor method
    def __init__(self, symbol=None, freq=0, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
        
    #less than operator method
    def __lt__(self, other):
        return self.freq < other.freq
        
def generate_frequency_table(symbols):
    symbol_count = Counter(symbols)
    total_count = len(symbols)
    frequency_table = []
    for symbol, count in symbol_count.items():
        probability = count / total_count
        node = Node(symbol, probability)
        frequency_table.append(node)

    #print the frequency table
    print("Frequency Table")
    for node in frequency_table:
        print(node.symbol, node.freq)

    return frequency_table
    
def build_huffman_tree(frequency_table):
    heap = frequency_table[:]

    
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)

        print("Left and Right")
        print(left.symbol, left.freq)
        print(right.symbol, right.freq)

        parent = Node(freq=left.freq+right.freq, left=left, right=right)
        heappush(heap, parent)

        # #print the HEAP
        # print("Frequency heap")
        # for node in heap:
        #     print(node.symbol, node.freq)

    return heap[0]

def generate_codewords(root):
    codewords = {}
    stack = [(root, "")]
    while stack:
        node, code = stack.pop()
        if node.symbol:
            codewords[node.symbol] = code
        if node.left:
            stack.append((node.left, code + "0")) 
        if node.right:
            stack.append((node.right, code + "1"))
    return codewords

def encode(symbols, codewords):
    encoded_message = ""
    for symbol in symbols:
        encoded_message += codewords[symbol]
    return encoded_message

def decode(encoded_message, root):
    decoded_message = ""
    node = root
    for bit in encoded_message:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.symbol:
            decoded_message += node.symbol
            node = root
    return decoded_message

# Read input from file
with open("input.txt", "r") as f:
    input_string = f.read()

# Generate frequency table
frequency_table = generate_frequency_table(input_string)

# Build Huffman tree
root = build_huffman_tree(frequency_table)

# Generate codewords
codewords = generate_codewords(root)

# Encode input string
encoded_message = encode(input_string, codewords)

# Decode encoded message
decoded_message = decode(encoded_message, root)

# Write codewords to file
with open("codewords.txt", "w") as f:
    for symbol, codeword in codewords.items():
        f.write(f"{symbol}: {codeword}\n")

# Write encoded message to file
with open("encoded.txt", "w") as f:
    f.write(encoded_message)

# Write decoded message to file
with open("decoded.txt", "w") as f:
    f.write(decoded_message)