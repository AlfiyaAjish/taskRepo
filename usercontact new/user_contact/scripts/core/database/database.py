from pymongo import MongoClient
# from scripts.config.application_config import MONGO_URI, DB_NAME

client = MongoClient("mongodb+srv://alfi:nAWTUfiTtCctlEAR@cluster123.mqa4d.mongodb.net/?retryWrites=true&w=majority&appName=cluster123")
db = client["user_contact_db"]
