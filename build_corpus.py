from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)
print("Connecting to db")
db = client.test
coll = db.toxicdocs_combined_vectorized
cursor = coll.find()
counter = 0


setList = []
for document in cursor:
    counter += 1
    print(counter)
    if document["text"] != []:
        text = document["text"]
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'[0-9]+', ' ', text)
        setList.append(" ".join(text.split()))
file = open('./glove/corpus.txt', 'w')
for doc in setList:
    file.writelines(doc+'\n')
file.close()
