from unittest import TestCase, main
from application.manager import Manager
import random, string
from application.mission_dao import MissionDao

class ManagerTest(TestCase):

    def test_manager_can_start_and_find(self):
        id = 'test_id_' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        manager = Manager()
        dao = MissionDao()
        valid_mission = {
            "mission" : {
                "id": id
            }
        }
        self.assertEqual(manager.is_started(valid_mission), False)
        manager.start_mission(valid_mission)
        self.assertEqual(manager.is_started(valid_mission), True)
        dao.remove_mission(valid_mission)




if __name__ == '__main__':
    main()