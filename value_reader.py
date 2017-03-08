from mission import Mission


class ValueReaderFactory():
    def __init__(self, mission):
        self.mission = mission

    def reader(self):
        '''
        :return: Reader for mission provided
        '''
        # changeit
        return StaticValueReader(self.mission)

class ValueReader:
    def __init__(self, mission):
        self.mission = mission

    # @abstract
    def read(self):
        '''
        reads value using config
        :return:
        '''


class StaticValueReader(ValueReader):

    def read(self):
        return self.mission['mission']['source']['static_value']
