import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import os
from collections import Counter

embeddings_dict = {}
NERs = []

with open('/home/ubuntu/relationship_visualizer/GloVe/vectors.txt', 'r', encoding="utf-8") as f:
    print('1')
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict.update({word: vector})
with open('/home/ubuntu/relationship_visualizer/NERs.txt', 'r') as f:
    print('2')
    for line in f:
        NERs.append(line.replace('\n', ''))
NERs = {k: v for k, v in dict(Counter(NERs)).items() if v >= 15}
NERs = list(NERs.keys())

keys = set(embeddings_dict.keys())
failed = []
def get_vector_average(word):
    split_word = word.lower().split(' ')
    try:
        vector = embeddings_dict[split_word[0]]
    except:
        print("fail1" + split_word[0])
        failed.append(word)
        return None
    for indiv in split_word[1:]:
        try:
            vector = vector + embeddings_dict[indiv] 
        except:
            # print(word)
            failed.append(indiv)
            return None
    print(word)
    return vector / len(split_word)

present = {}

counter = 0
for x in NERs:
    counter += 1

    avg_vector = get_vector_average(x)
    present.update({x: avg_vector})

print('4')

with open('/home/ubuntu/relationship_visualizer/GloVe/failed.txt', 'w') as w:
    w.write(' '.join(failed))
with open('/home/ubuntu/relationship_visualizer/GloVe/NER_vectors.txt', 'w') as f:
    for element in present.keys():
        if present[element] is not None:
            f.write(element + ' ' + np.array2string(present[element], separator=' ') + '\n')
        # f.write(str(element) + ' ' + ' '.join(str(v) for v in embeddings_dict[element].tolist()) + '\n')


