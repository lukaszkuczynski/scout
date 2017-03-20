from application.mission import Mission
from application.notepad import DefaultNotepad, InMemoryNotepad
from application.value_reader import ValueReaderFactory
from application.criteria import CriteriaFactory
from application.research import ResearchResult
from application.notifier import NotifierFactory
from application.reporter import ReporterFactory

class Scout:

    def __read_mission(self, mission_id):
        return Mission()

    def notepad_for_mission(self, mission):
        if 'notepad' in mission['mission']:
            if 'in_memory' in mission['mission']['notepad']:
                return InMemoryNotepad()
            else:
                return DefaultNotepad()
        else:
            return DefaultNotepad()

    def __read_notes(self, mission):
        '''
        Collects notes from previous mission attempts from datastore
        :param mission: mission in progess
        :return: notes read
        '''
        notepad = self.notepad_for_mission(mission)
        notepad.read_for_mission(mission)

    def __do_research(self, mission, notes):
        '''
        Runs research using notes read from previous steps
        :param mission: mission in progress
        :param notes: notes from previous runs
        :return: research results
        '''
        value_reader = ValueReaderFactory(mission).reader()
        criteria = CriteriaFactory(mission).criteria()
        notifier = NotifierFactory(mission).notifier()

        current_value = value_reader.read()
        match = criteria.test(current_value)
        if match.found:
            notification = notifier.verify(current_value, notes)
            if notification.should_notify:
                return ResearchResult.FOUND(current_value)
            else:
                return ResearchResult.FOUND_BUT_KEEP_SILENT(current_value)
        else:
            return ResearchResult.NOT_FOUND()


    def __send_report_if_needed(self, mission, research_results):
        '''
        If results has significant changes, send report for that mission
        :param research_results: results from research
        :return: results returned to update notes
        '''
        if research_results.found():
            ReporterFactory(mission).reporter().report(research_results.current_value)

    def __update_notes(self, mission, research_result):
        '''
        Update notes on persistent storage that will be needed for the next attempt
        :param research_result
        :return:
        '''
        notepad = self.notepad_for_mission(mission)
        notepad.save_for_mission(mission, research_result)

    def attempt(self, mission_id):
        mission = self.__read_mission(mission_id)
        return self.attempt_mission(mission)

    def attempt_mission(self, mission):
        notes = self.__read_notes(mission)
        research_result = self.__do_research(mission, notes)
        self.__send_report_if_needed(mission, research_result)
        self.__update_notes(mission, research_result)
        return research_result
