import pickle
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

glove_file = datapath('/home/ubuntu/relationship_visualizer/tsne_list.txt')
word2vec_glove_file = get_tmpfile("tsne_list_word2vec.txt")
glove2word2vec(glove_file, word2vec_glove_file)

model = KeyedVectors.load_word2vec_format(word2vec_glove_file)

filename = 'tsne_list.sav'
pickle.dump(model, open(filename, 'wb'))
