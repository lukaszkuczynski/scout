from mission import Mission


class CriteriaFactory:
    def __init__(self, mission):
        self.mission = mission

    def criteria(self):
        '''
        should return instance of correct Comparator based on mission
        '''
        # change it
        return CriteriaContains(self.mission)


class Criteria:
    '''Abstract comparator'''

    def __init__(self, mission):
        '''
        should
        :param mission:
        '''
        self.mission = mission

    def test(self, value):
        '''
        takes original value and current one and returns calculation of difference between them
        :param previous:
        :param current:
        :return:
        '''
        return None


class Match:
    def __init__(self, found):
        self.found = found


class CriteriaContains(Criteria):
    def test(self, value):
        tested_text = self.mission['mission']['compare']['contains']
        if tested_text in value:
            return Match(True)
        else:
            return Match(False)