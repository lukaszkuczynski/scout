from unittest import TestCase, main
from application.scout import Scout


class ScoutDumbTest(TestCase):

    mission = {
        "mission": {
            "name" : "is ow part of Wow",
            "source": {
                "static_value": "Wow"
            },
            "compare" : {
                "contains": "ow"
            },
            "notify": "always",
            "report": "console"
        }
    }

    def test_dumb(self):
        scout = Scout()
        research = scout.attempt_mission(self.mission)
        self.assertTrue(research.found())

if __name__ == '__main__':
    main()