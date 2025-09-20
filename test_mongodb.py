from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://123karthikns:Karthi123@cluster0.97zewqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)