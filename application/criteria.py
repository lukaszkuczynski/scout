from application.mission import Mission


class CriteriaFactory:
    def __init__(self, mission):
        self.config = mission['mission']['compare']

    def criteria(self):
        '''
        should return instance of correct Comparator based on mission
        '''
        # change it
        if "contains" in self.config:
            return CriteriaContains(self.config["contains"])
        elif "similar" in self.config:
            return CriteriaSimilar(self.config["similar"])


class Criteria:
    '''Abstract comparator'''

    def __init__(self, config):
        '''
        should
        :param mission:
        '''
        self.config = config

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
        tested_text = self.config
        if tested_text in value:
            return Match(True)
        else:
            return Match(False)


class CriteriaSimilar(Criteria):
    def test(self, value):
        from application.similarity_calculator import SimilarityCalculator
        calculator = SimilarityCalculator()
        tested_text = self.config
        if calculator.are_similar(value, tested_text):
            return Match(True)
        else:
            return Match(False)