from pymongo import MongoClient

URI = 'mongodb+srv://enzo:admin123@goapi.mqcds.mongodb.net/GoAPI?retryWrites=true&w=majority'

DATABASE = 'Training'


class DataBase:
    def __init__(self, collection):
        self.client = None
        self.connect(collection)

    def connect(self, collection):
        self.client = MongoClient(URI)[DATABASE][collection]

    def find(self):
        doc_counter = self.client.count_documents({})
        if doc_counter:
            return self.client.find({})
        return False

    def find_one(self, doc):
        return self.client.find_one(doc)

    def insert_one(self, doc):
        return self.client.insert_one(doc)

    def update_one(self, index, doc):
        return self.client.update_one(index, doc)
