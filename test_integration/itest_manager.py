from unittest import TestCase, main
from application.manager import Manager

class ManagerTest(TestCase):

    def test_manager_can_start(self):
        manager = Manager()
        valid_mission = {
            "mission" : {
                "id": "some_id"
            }
        }
        manager.start_mission(valid_mission)
        self.assertEqual(manager.is_started(valid_mission), True)


if __name__ == '__main__':
    main()