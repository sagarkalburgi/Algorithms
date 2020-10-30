# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 19:45:31 2020

@author: LENOVO
"""

from heapq import heappop,heappush,heapify
from collections import defaultdict
from bitarray import bitarray

text = "HELLO WORLD"

# Dictionary with frequency of each symbols
freq_lib = defaultdict(int)     # Generates default libraries
for ch in text:
    freq_lib[ch] += 1
print(freq_lib)

# Creat Huffman Tree
heap = [[count,[sym,""]] for sym, count in freq_lib.items()]        # "" used for entering huffman code later
print(heap)

heapify(heap)       # transform the list into a heap tree structure
print(heap)

while len(heap) > 1:
    right = heappop(heap)       # heappop - pop and return the smallest item from the heap
    print('right = ',right)
    left = heappop(heap)
    print('left = ',left)
    print('')
    
    for pair in right[1:]:
        pair[1] = '1' + pair[1]     # add one to all the right branches
    print('right add one = ', right)
    for pair in left[1:]:
        pair[1] = '0' + pair[1]     # add zero to all the left branches
    print('left add zero = ',left)
    print('')
    
    heappush(heap,[right[0] + left[0]] + right[1:] + left[1:])      # add values into heap Eg heappush(h,(5,'writecode')) --> h = [(5,'writecode')]

huffman_list = right[1:] + left[1:]
print(huffman_list)
print('')
huffman_dict = {a[0]:bitarray(str(a[1])) for a in huffman_list}
print(huffman_dict)
print('')

# Huffman Encoding

encoded_text = bitarray()
encoded_text.encode(huffman_dict,text)
print(encoded_text)
print(len(encoded_text))

# Padding
padding = 8- (len(encoded_text)%8)
print("Padding:",padding)

# save encoded text as binary file
with open('compressed_file.bin','wb') as w:
    encoded_text.tofile(w)

# Decoding
decoded_text = bitarray()

with open('compressed_file.bin','rb') as r:
    decoded_text.fromfile(r)

decoded_text = decoded_text[:-padding]
decoded_text = decoded_text.decode(huffman_dict)
decoded_text = ''.join(decoded_text)
print(decoded_text)

# save an uncompressed file for comparison
with open('uncompressed.bin','w') as w:
    w.write(text)