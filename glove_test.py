import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
coll = db.NER_vectors
cursor = coll.find()

embeddings_dict = {} # load in vectors
for document in cursor:
    word = document["word"]
    temp = document["vector"].split(" ")
    temp = ' '.join(temp).split()
    values = np.array(temp)
    vector = values.astype(np.float)
    embeddings_dict.update({word: vector})
# with open('/home/ubuntu/relationship_visualizer/GloVe/vectors.txt', 'r', encoding="utf-8") as f:
#     for line in f:
#         values = line.split()
#         word = values[0]
#         vector = np.asarray(values[1:], "float32")
#         embeddings_dict[word] = vector

def find_closest(embedding):
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))

# print(find_closest(embeddings_dict['Monsanto'])[1:10])

tsne = TSNE(n_components=2, random_state=0, perplexity=100, n_iter=1000)
words = list(embeddings_dict.keys())
vectors = [embeddings_dict[word] for word in words]
Y = tsne.fit_transform(vectors)
# np.save('tsne.py', Y)
plt.scatter(Y[:, 0], Y[:, 1], 0.2)

for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
    plt.annotate(label, xy=(x*1000, y*1000), xytext=(0,0), textcoords="offset points", fontsize=5)
plt.savefig('glove_test_P100_I1000.png', dpi=5000)
