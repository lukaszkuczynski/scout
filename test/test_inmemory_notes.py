from unittest import main, TestCase
from application.notepad import InMemoryNotepad


class InMemoryNotesTest(TestCase):

    def test_notes_after_add_contains_notes(self):
        notes = InMemoryNotepad()

        mission = {
            'id': 'this_is_id'
        }
        note = 'This is good note'

        notes.add_for_mission(mission, note)
        notes_read = notes.read_for_mission(mission)
        self.assertIn('This is good note', notes_read)


if __name__ == '__main__':
    main()