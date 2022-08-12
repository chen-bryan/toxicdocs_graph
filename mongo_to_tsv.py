# Saving vectors in tsv format for use with tensorboard
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
coll = db.NER_vectors
cursor = coll.find()
words = []
vectors = []
counter = 0
for document in cursor:
    word = document["word"]
    vector = '    '.join(document["vector"].split())
    counter += 1
    words.append(word)
    vectors.append(vector)
print(counter)
with open('vectors.tsv', 'w') as f:
    for item in vectors:
        f.write(f'{item}\n')

with open('metadatafull.tsv', 'w') as f:
    for item in words:
        f.write(f'{item}\n')

