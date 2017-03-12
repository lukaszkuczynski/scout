class ResearchStatus():

    @staticmethod
    def FOUND():
        return 0;

    @staticmethod
    def FOUND_BUT_KEEP_SILENT():
        return 1;

    @staticmethod
    def NOT_FOUND():
        return 2;


class ResearchResult:

    def __init__(self, status, current_value):
        self.status = status
        self.current_value = current_value

    def found(self):
        return self.status == ResearchStatus.FOUND()

    @staticmethod
    def FOUND(current):
        return ResearchResult(ResearchStatus.FOUND(), current)

    @staticmethod
    def FOUND_BUT_KEEP_SILENT(current):
        return ResearchResult(ResearchStatus.FOUND_BUT_KEEP_SILENT(), current)

    @staticmethod
    def NOT_FOUND():
        return ResearchResult(ResearchStatus.NOT_FOUND(), None)