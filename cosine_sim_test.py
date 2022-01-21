from pymongo import MongoClient
import sys
import networkx as nx
from networkx.readwrite import json_graph
from itertools import combinations

def combine_dicts(dict1, dict2):
        for key in dict2.keys():
                try:
                        dict1[key].append(dict2[key])
                except:
                        dict1.update(dict2[key])
        return key


client = MongoClient('localhost', 27017)
print("Connecting to db")
db = client.test
coll = db.toxicdocs_combined_vectorized

key_name = "Elmer Wheeler"
cursor = coll.find()
data = {}
entities = {}
counter = 0
for document in cursor:
	counter += 1
	print(counter)
	if document["Ensemble_PEOPLE"] != []:
		data.update({document["_id"]: document["Ensemble_PEOPLE"]})

for ID in data:
	people = data[ID]
	for person in people:
                if person not in entities.keys():
                        entities.update({person: 1})
                else:
                        try:
                                entities[person] += 1
                        except:
                                entities.update({person: 1})

for person in list(entities):
        if entities[person] < 15: #arbitrary cutoff value
                entities.pop(person)

print(len(entities))
print(sys.getsizeof(entities))
g = nx.Graph()


