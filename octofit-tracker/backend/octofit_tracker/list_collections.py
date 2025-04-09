from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient('mongodb://localhost:27017/')

# Access the database
db = client['octofit_db']

# List all collections in the database
collections = db.list_collection_names()

print("Collections in octofit_db:", collections)

# Verify the data in the database
for collection_name in db.list_collection_names():
    print(f"Collection: {collection_name}")
    documents = db[collection_name].find()
    for document in documents:
        print(document)