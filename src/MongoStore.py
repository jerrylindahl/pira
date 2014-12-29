import datetime
from pymongo import MongoClient


class MongoStore:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.pira

        # Get status from last run
        self.status = self.get_status()

        if self.status is None:
            print("Empty database, starting new datastore.")
            self.init_store()
            self.status = self.get_status()

        print(self.status)

    def mongo(self):

        c = self.db.issues
        #key = c.insert({"id": "MFOL-123"})
        #print(key)
        i = c.find_one()
        print(i)

    def init_store(self):
        self.status = {"last_run": datetime.datetime.now()}
        s = self.db.status
        s.insert(self.status)

    def get_status(self):
        s = self.db.status
        return s.find_one()