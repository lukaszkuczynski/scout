import os
from pymongo import MongoClient

class MissionDao:

    def __init__(self):
        if not 'SCOUT_MONGO_HOST' in os.environ:
            raise Exception("Scout expects SCOUT_MONGO_HOST set in environment")
        self.host = os.environ['SCOUT_MONGO_HOST']
        if not 'SCOUT_MONGO_PORT' in os.environ:
            raise Exception("Scout expects SCOUT_MONGO_PORT set in environment")
        self.port = int(os.environ['SCOUT_MONGO_PORT'])
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client['scout']
        assert "scout" in self.client.database_names()
        assert "mission" in self.db.collection_names()


    def create_mission(self, mission):
        self.db.mission.insert(mission['mission'])

    def find_mission(self, mission):
        id = mission['mission']['id']
        found = self.db.mission.find_one({"id": id})
        return found

    def remove_mission(self, mission):
        id = mission['mission']['id']
        found = self.db.mission.remove({"id": id})
        return found

