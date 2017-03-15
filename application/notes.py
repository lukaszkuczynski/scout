from abc import abstractmethod


class Notes:
    def __init__(self):
        self.previous_value = ''

    @abstractmethod
    def save_for_mission(self, mission, notes):
        pass

    def read_for_mission(self, mission):
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

