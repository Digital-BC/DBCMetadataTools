from pymongo import MongoClient

#Retrieves _id from Mongo items using the internal_identifier

uri = "YOUR MONGO CLUSTER"



# Connect to the MongoDB Atlas cluster
client = MongoClient(uri)
db = client['supplejack_api_production']
collection = db['records']



# List of internal_identifiers to be deleted
internal_identifiers = [
"https://viurrspace.ca/handle/10613/24880",
"https://viurrspace.ca/handle/10613/24920",
#. . . 
]

# Function to find and print documents by internal_identifier
def find_documents_by_internal_identifier(internal_identifiers):
    documents = collection.find({"internal_identifier": {"$in": internal_identifiers}}, {"_id": 1, "internal_identifier": 1})
    for doc in documents:
         print(doc["_id"])





# Call the function to test retrieval
find_documents_by_internal_identifier(internal_identifiers)
