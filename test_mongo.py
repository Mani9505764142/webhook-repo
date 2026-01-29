from pymongo import MongoClient

uri = "mongodb+srv://manikantasuthari2002_db_user:Sai253173@cluster0.smlcjp1.mongodb.net/github_events?appName=Cluster0"
client = MongoClient(uri, serverSelectionTimeoutMS=5000)

print("Connected successfully")
print(client.list_database_names())
