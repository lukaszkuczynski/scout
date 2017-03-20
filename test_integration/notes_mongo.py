from unittest import TestCase, main
from application.notepad import DefaultNotepad
import os
from pymongo import MongoClient


class NotepadMongoTest(TestCase):

    def setUp(self):
        os.environ['SCOUT_MONGO_HOST'] = 'localhost'
        os.environ['SCOUT_MONGO_PORT'] = '27017'
        self.mission = {
            "mission": {
                "id": "integration_test_mission",
                "notify": {
                    "distinct_field": {
                        "field": "url"
                    }
                }
            }
        }

    def test_server_returns_info(self):
        notepad = DefaultNotepad()
        notepad.check_status()

    def test_notepad_can_read(self):
        notepad = DefaultNotepad()
        notes = notepad.read_for_mission(self.mission)
        self.assertIsNotNone(notes)
        self.assertIn("new_url.com", notes)

    def remove_mission(self, id):
        db = MongoClient().scout.notes
        found = db.find_one({'mission_id': id})
        db.delete_one({'mission_id': id})
        return found

    def test_notepad_can_save_when_empty(self):
        notepad = DefaultNotepad()
        deleted = self.remove_mission(self.mission['mission']['id'])
        print(deleted)
        notes = notepad.read_for_mission(self.mission)
        self.assertIsNone(notes)
        notes = { 'url': 'new_url.com' }
        notepad.save_for_mission(self.mission, notes)
        notes = notepad.read_for_mission(self.mission)
        self.assertIn('new_url.com', notes)

    def test_notepad_can_add_new_value_when_existing(self):
        notepad = DefaultNotepad()
        mission = {
            "mission": {
                "id": "integration_test_mission",
                "notify": {
                    "distinct_field": {
                        "field": "url"
                    }
                }
            }
        }
        old_notes = notepad.read_for_mission(mission)
        self.assertIsNotNone(old_notes)
        notes = { 'url': 'brandnew_url.com' }
        notepad.save_for_mission(mission, notes)
        notes = notepad.read_for_mission(mission)
        self.assertIn( "brandnew_url.com", notes )
        notepad.reset_notes_at(mission, {'url': old_notes})


if __name__ == '__main__':
    main()