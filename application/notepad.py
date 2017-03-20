from abc import abstractmethod
from pymongo import MongoClient
import os


class Notepad:
    def __init__(self):
        self.previous_value = ''

    @abstractmethod
    def save_for_mission(self, mission, notes):
        pass

    @abstractmethod
    def read_for_mission(self, mission):
        pass

    @abstractmethod
    def check_status(self):
        pass


class InMemoryNotepad(Notepad):

    def __init__(self):
        self.notes = {}

    def add_for_mission(self, mission, notes):
        if not mission['id'] in self.notes:
            self.notes[mission['id']] = []
        self.notes[mission['id']].append(notes)

    def read_for_mission(self, mission):
        id = mission['id']
        return self.notes[id]


class DefaultNotepad(Notepad):

    def __init__(self):
        if not 'SCOUT_MONGO_HOST' in os.environ:
            raise Exception("Scout expects SCOUT_MONGO_HOST set in environment")
        self.host = os.environ['SCOUT_MONGO_HOST']
        if not 'SCOUT_MONGO_PORT' in os.environ:
            raise Exception("Scout expects SCOUT_MONGO_PORT set in environment")
        self.port = int(os.environ['SCOUT_MONGO_PORT'])
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client['scout']

    def check_status(self):
        print("checking mongo server")
        print(self.client.server_info())
        assert "scout" in self.client.database_names()
        assert "notes" in self.db.collection_names()

    def save_for_mission(self, mission, notes):
        # if mission.has_notifier_with_distinct_value()
        # if "distinct_field" in mission['mission']['notify']:
        pass

    def read_for_mission(self, mission):
        id = mission['mission']['id']
        value = self.db.notes.find_one({"mission_id": id})
        return value
