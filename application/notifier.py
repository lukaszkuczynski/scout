class NotifierFactory:
    def __init__(self, mission):
        self.mission = mission

    def notifier(self):
        return NotifierAlways()


class Notification:
    def __init__(self, should):
        self.should_notify = True

class Notifier:
    def verify(self, current, notes):
        return None;

class NotifierAlways(Notifier):
    def verify(self, current, notes):
        return Notification(True)