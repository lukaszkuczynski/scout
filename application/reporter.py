from abc import abstractmethod

class ReporterFactory:
    def __init__(self, mission):
        self.config = mission['mission']['reporter']

    def reporter(self):
        from application.mail_reporter import MailReporter
        if 'console' in self.config:
            return ConsoleReporter()
        elif 'mail' in self.config:
            return MailReporter(self.config['mail'])
        else:
            raise Exception('unknown reporter')


class Reporter:
    @abstractmethod
    def report(self, value):
        pass


class ConsoleReporter(Reporter):
    def report(self, value):
        print("Found value matching criteria! "+value)