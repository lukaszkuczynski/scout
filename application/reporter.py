class ReporterFactory:
    def __init__(self, mission):
        self.mission = mission

    def reporter(self):
        return ConsoleReporter()


class Reporter:
    def report(self, value):
        pass


class ConsoleReporter(Reporter):
    def report(self, value):
        print("Found value matching criteria! "+value)