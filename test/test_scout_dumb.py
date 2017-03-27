from unittest import TestCase, main, skip
from application.scout import Scout


class ScoutDumbTest(TestCase):

    mission = {
        "mission": {
            "id" : "is_ow_part_of_Wow",
            "notepad" : "in_memory",
            "source": {
                "static_value": "Wow"
            },
            "compare" : {
                "contains": "ow"
            },
            "notify": "always",
            "reporter": "console"
        }
    }

    def test_dumb(self):
        scout = Scout()
        research = scout.attempt_mission(self.mission)
        self.assertTrue(research.found())

if __name__ == '__main__':
    main()