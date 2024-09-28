from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://211420:abcd1234@cluster0.kfl3u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "wysa_db"

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]