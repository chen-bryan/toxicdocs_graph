import pickle
import networkx as nx
import plotly
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from sklearn.manifold import TSNE
from pyvis.network import Network

filename = 'super_stripped_glove2word2vec_model.sav'
model = pickle.load(open(filename, 'rb'))

def append_list(sim_words, words):
    list_of_words = []

    for i in range(len(sim_words)):
        sim_words_list = list(sim_words[i])
        sim_words_list.append(words)
        sim_words_tuple = tuple(sim_words_list)
        list_of_words.append(sim_words_tuple)
    return list_of_words

key_word = ['EPA']

def gen_similarity(user_input, iterations):
    result_word = []
    for words in user_input:
        sim_words = model.most_similar(words, topn = iterations)
        sim_words = append_list(sim_words, words)
        result_word.extend(sim_words)
    similar_word = [word[0] for word in result_word]
    similarity = [word[1] for word in result_word]
    similar_word.extend(user_input)
    labels = [word[2] for word in result_word]
    label_dict = dict([(y,x+1) for x,y in enumerate(set(labels))])
    color_map = [label_dict[x] for x in labels]
    return result_word, similar_word, similarity, similar_word, labels, label_dict, color_map


result_word, similar_word, similarity, similar_word, labels, label_dict, color_map = gen_similarity(key_word, 2000)
result_word_2, similar_word_2, similarity_2, similar_word_2, labels_2, label_dict_2, color_map_2 = gen_similarity(similar_word, 100)
elist = []
for a, b, c in result_word:
    if b > 0.25:
        elist.append((a, c, b*100))
for a, b, c in result_word_2:
    if b > 0.25:
        elist.append((a, c, b*100))
g = nx.DiGraph()
g.add_weighted_edges_from(elist, mass=1000)
net = Network()
net.from_nx(g)
net.barnes_hut(gravity=-8000, central_gravity=1, spring_length=500, spring_strength=0.001, damping=0.09, overlap = 0)
net.save_graph('test.html')

for (u, v, wt) in g.edges.data('weight'):
    print(f"({u}, {v}, {wt:.3})")
print(len(elist))
exit()