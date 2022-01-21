from pymongo import MongoClient
#from apriori_python import apriori
from efficient_apriori import apriori

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
    if counter == 100:
        break
    if document["Ensemble_PLACES"] != []:
        setList.append(tuple(document["Ensemble_PLACES"]))
print(setList[0:100])
#transactions = [('eggs', 'bacon', 'soup', 'bad'),('eggs', 'bacon', 'apple'),('soup', 'bacon', 'banana')]
itemset, rules = apriori(setList[0:100], min_support=0, min_confidence=0.5)
#itemset, rules = apriori(transactions, min_support=0.2, min_confidence=0.2)
print(itemset)
print(rules)
