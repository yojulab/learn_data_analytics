from pymongo import MongoClient

# MongoDB connection information
host = 'your_mongodb_host'
port = 27017
username = 'your_username'
password = 'your_password'
database = 'your_database'

# Create a MongoDB client
client = MongoClient(host, port)

# Access the specified database
db = client[database]

# Authenticate with username and password
db.authenticate(username, password)

# Perform database operations
# For example, fetch all documents from a collection
collection = db['your_collection']
documents = collection.find({})

for document in documents:
    print(document)

# Close the MongoDB connection
client.close()