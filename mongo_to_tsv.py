# Saving vectors in tsv format for use with tensorboard
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
coll = db.NER_vectors
cursor = coll.find()
words = []
vectors = []
for document in cursor:
    word = document["word"]
    vector = document["vector"].split(" ")
    vector = "\\t".join(vector)
    
    words.append(word)
    vectors.append(vector)

with open('vectors.tsv', 'w') as f:
    for item in vectors:
        f.write(f'{item}\n')

with open('metadata.tsv', 'w') as f:
    for item in words:
        f.write(f'{item}\n')
