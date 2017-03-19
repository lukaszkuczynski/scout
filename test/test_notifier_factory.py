from unittest import TestCase, main
from application.notifier import NotifierFactory, NotifierAlways, NotifierDistinctField

class NotifierFactoryTest(TestCase):

    def test_factory_returns_always(self):
        mission = {
            "mission": {
                "notify" : "always"
            }
        }
        notifier = NotifierFactory(mission).notifier()
        self.assertIsInstance(notifier, NotifierAlways)


    def test_factory_returns_distinct_field(self):
        mission = {
            "mission": {
                "notify" : {
                    "distinct_field": ["field1"]
                }
            }
        }
        notifier = NotifierFactory(mission).notifier()
        self.assertIsInstance(notifier, NotifierDistinctField)


if __name__ == '__main__':
    main()