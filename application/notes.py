from abc import abstractmethod
from pymongo import MongoClient
import os


class Notes:
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


class InMemoryNotes(Notes):

    def __init__(self):
        self.notes = {}

    def add_for_mission(self, mission, notes):
        if not mission['id'] in self.notes:
            self.notes[mission['id']] = []
        self.notes[mission['id']].append(notes)

    def read_for_mission(self, mission):
        id = mission['id']
        return self.notes[id]


class DefaultNotes(Notes):

    def __init__(self):
        if not 'SCOUT_MONGO_HOST' in os.environ:
            raise Exception("Scout expects SCOUT_MONGO_HOST set in environment")
        self.host = os.environ['SCOUT_MONGO_HOST']
        if not 'SCOUT_MONGO_PORT' in os.environ:
            raise Exception("Scout expects SCOUT_MONGO_PORT set in environment")
        self.port = int(os.environ['SCOUT_MONGO_PORT'])

    def check_status(self):
        client = MongoClient(host=self.host, port=self.port)
        print("checking mongo server")
        print(client.server_info())

    def save_for_mission(self, mission, notes):
        pass

    def read_for_mission(self, mission):
        pass
