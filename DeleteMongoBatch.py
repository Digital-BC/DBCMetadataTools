from pymongo import MongoClient

#Deletes Mongo items via  'internal_identifier

uri = "YOUR MONGO CLUSTER"

# Connect to the MongoDB Atlas cluster
client = MongoClient(uri)
db = client['supplejack_api_production']
collection = db['records']


# List of internal_identifiers to be deleted
internal_identifiers = [
"https://viurrspace.ca/handle/10613/24880",
"https://viurrspace.ca/handle/10613/24920" 
#. . . 
]

# Function to find and print documents by internal_identifier
def find_and_print_documents(internal_identifiers):
    documents = collection.find({"internal_identifier": {"$in": internal_identifiers}}, {"_id": 1, "internal_identifier": 1})
    for doc in documents:
        print(f'Found document - _id: {doc["_id"]}, internal_identifier: {doc["internal_identifier"]}')

# Function to delete documents by internal_identifier
def delete_documents(internal_identifiers):
    result = collection.delete_many({"internal_identifier": {"$in": internal_identifiers}})
    print(f'Deleted {result.deleted_count} documents.')

# Verify documents before deletion
find_and_print_documents(internal_identifiers)

# Perform the deletion
delete_documents(internal_identifiers)
