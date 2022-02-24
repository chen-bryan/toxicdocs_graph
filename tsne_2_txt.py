import numpy as np

tsne = np.load('/home/ubuntu/relationship_visualizer/tsne.py.npy')
with open('word_list.txt', 'r') as f:
    words = f.read().splitlines()
words = list(map(lambda x: x[ : -1], words))

file = open("tsne_list.txt", "a")
for label, x, y in zip(words, tsne[:, 0], tsne [:, 1]):
    x = "{:.6f}".format(x)
    y = "{:.6f}".format(y)
    label = label.replace(" ", "_")
    file.write(label + " " + x + " " + y + "\n")

file.close()
