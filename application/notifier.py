from abc import abstractmethod

class NotifierFactory:
    def __init__(self, mission):
        self.config = mission['mission']['notify']

    def notifier(self):
        if "always" in self.config:
            return NotifierAlways(self.config)
        elif "distinct_field" in self.config:
            return NotifierDistinctField(self.config["distinct_field"])


class Notification:
    def __init__(self, should):
        self.should_notify = should


class Notifier:
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def verify(self, current, notes):
        return None;


class NotifierAlways(Notifier):
    def verify(self, current, notes):
        return Notification(True)


class NotifierDistinctField(Notifier):
    def verify(self, current, notes):
        field = self.config['field']
        all_values = []
        if field in notes:
            all_values = notes[field]
        current_value = current[field]
        if current_value not in all_values:
            return Notification(True)
        else:
            return Notification(False)
