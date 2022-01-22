from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)
print("Connecting to db")
db = client.test
coll = db.NER_vectors
cursor = coll.find()
counter = 0


all = ""
with open('/home/ubuntu/relationship_visualizer/GloVe/NER_vectors.txt', 'r') as f:
    for line in f:
        all += line.rstrip('\n')

NERs = re.split('\[|\]', all)

words = {}
num = len(NERs)
while counter < num:
    counter += 2
    if counter % 2 == 0:
        try:
            temp = {"word": NERs[counter], "vector": NERs[counter+1].rstrip('\n')}
        except IndexError as e:
            print("Done")
       
        x = coll.insert_one(temp)
