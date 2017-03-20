from unittest import TestCase, main
from application.notepad import DefaultNotepad
import os


class NotepadMongoTest(TestCase):

    def setUp(self):
        os.environ['SCOUT_MONGO_HOST'] = 'localhost'
        os.environ['SCOUT_MONGO_PORT'] = '27017'

    def test_server_returns_info(self):
        notepad = DefaultNotepad()
        notepad.check_status()

    def test_notepad_can_read(self):
        notepad = DefaultNotepad()
        mission = {
            "mission": {
                "id": "integration_test_mission"
            }
        }
        notes = notepad.read_for_mission(mission)
        self.assertIsNotNone(notes)
        print(notes)
        self.assertIn("someurl.com", notes['url'])


if __name__ == '__main__':
    main()