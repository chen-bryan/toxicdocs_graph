from pymongo import MongoClient

client = MongoClient('localhost', 27017)
print("Connecting to db")
db = client.test
coll = db.toxicdocs_combined_vectorized
cursor = coll.find()
counter = 0


NERs = []
for document in cursor:
    counter += 1
    print(counter)
    for e in document["Ensemble_PEOPLE"]:
        NERs.append(e)
    for e in document["Ensemble_PLACES"]:
        NERs.append(e)
    for e in document["Ensemble_ORGANIZATIONS"]:
        NERs.append(e)

textfile = open("NERs.txt", "w")
for element in NERs:
    textfile.write(element + "\n")
textfile.close()
