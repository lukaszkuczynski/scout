CODE_OK = 0
CODE_MISSION_IN_PROGRESS = 1
CODE_INVALID_SETTINGS = 2


class Mission:
    pass


class Manager:

    def __validate(self, settings):
        return True


    def __is_started(self,mission):
        return False


    def __msg(self, code, msg=''):
        return tuple(code, msg)


    def __set_schedule(self,mission):
        '''
        Place to set up cron or other scheduler settings to make automatic mission attempts for Scout
        :param mission:
        :return:
        '''
        pass

    def __unmarshal(self, settings):
        return Mission()

    def start_mission(self, settings):
        if not self.__validate(settings):
            return self.__msg(CODE_INVALID_SETTINGS)
        mission = self.__unmarshal(settings)
        if self.__is_started(mission):
            return (CODE_MISSION_IN_PROGRESS, mission)
        self.__set_schedule()
        return self.__msg(CODE_OK)
