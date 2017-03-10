from mission import Mission
from abc import abstractmethod


class ValueReaderFactory():
    def __init__(self, mission):
        self.config = mission['mission']['source']

    def reader(self):
        '''
        :return: Reader for mission provided
        '''
        # changeit
        if 'websimple' in self.config:
            return WebSimpleReader(self.config)


class ValueReader:
    def __init__(self, mission):
        self.mission = mission

    @abstractmethod
    def read(self):
        pass


class StaticValueReader(ValueReader):

    def read(self):
        return self.config['static_value']


class WebSimpleReader(ValueReader):

    def read(self):
        pass
