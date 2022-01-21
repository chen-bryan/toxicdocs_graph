import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import os
from collections import Counter

embeddings_dict = {}
NERs = []
with open('/home/ubuntu/relationship_visualizer/glove/vectors.txt', 'r', encoding="utf-8") as f:
    print('1')
    for line in f:
        values = line.split()
        word = values[0]
        vector = values[1:]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict[word] = vector

with open('/home/ubuntu/relationship_visualizer/NERs.txt', 'r') as f:
    print('2')
    for line in f:
        NERs.append(line.replace('\n', ''))

NERs = {k: v for k, v in dict(Counter(NERs)).items() if v >= 50}
NERs = list(NERs.keys())
print(NERs)
keys = set(embeddings_dict.keys())
present = []
counter = 0
for x in NERs:
    counter += 1
    if counter % 100 == 0:
        print(counter)
    for ele in keys:
        if x in ele:
            present.append(ele)
present = list(set(present))
print(present)
sorted_present = []
for ele in NERs:
    print(ele)
    if ele in present:
        sorted_present.append(ele)
print('4')
with open('/home/ubuntu/relationship_visualizer/glove/stripped_vectors.txt', 'w') as f:
    for element in sorted_present:
        f.write(str(element) + ' ' + ' '.join(str(v) for v in embeddings_dict[element].tolist()) + '\n')


