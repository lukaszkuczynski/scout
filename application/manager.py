from application.mission_dao import MissionDao

CODE_OK = 0
CODE_MISSION_IN_PROGRESS = 1
CODE_INVALID_SETTINGS = 2


class Mission:
    pass


class Manager:

    def __init__(self):
        self.dao = MissionDao()

    def __validate(self, settings):
        return True


    def is_started(self, mission):
        found = self.dao.find_mission(mission)
        return found is not None


    def __msg(self, code, msg=''):
        return (code, msg)


    def __set_schedule(self,mission):
        self.dao.create_mission(mission)
        '''
        Place to set up cron or other scheduler settings to make automatic mission attempts for Scout
        :param mission:
        :return:
        '''


    def start_mission(self, mission):
        if not self.__validate(mission):
            return self.__msg(CODE_INVALID_SETTINGS)
        if self.is_started(mission):
            return (CODE_MISSION_IN_PROGRESS, mission)
        self.__set_schedule(mission)
        return self.__msg(CODE_OK)
