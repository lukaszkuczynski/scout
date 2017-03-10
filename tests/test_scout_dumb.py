from unittest import TestCase, main
from scout import Scout
import json
from mission import Mission


class ScoutDumbTest(TestCase):

    def test_dumb(self):
        scout = Scout()
        with open('mission_dumb.json') as mission_config:
            mission = Mission(json.load(mission_config))
            research = scout.attempt_mission(mission)
            self.assertTrue(research.found())

if __name__ == '__main__':
    main()