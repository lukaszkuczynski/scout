from unittest import TestCase, main
from application.notes import DefaultNotes
import os

class NotesMongoTest(TestCase):

    def test_server_returns_info(self):
        os.environ['SCOUT_MONGO_HOST'] = 'localhost'
        os.environ['SCOUT_MONGO_PORT'] = '27017'
        notes = DefaultNotes()
        notes.check_status()


if __name__ == '__main__':
    main()