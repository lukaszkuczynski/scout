from unittest import TestCase, main
from application.notifier import NotifierFactory


class NotifierDistinctFieldTest(TestCase):

    def test_notifier_notifies_when_no_notes(self):
        mission = {
            "mission": {
                "notify": {
                    "distinct_field": {
                        "field" : "url"
                    }
                }
            }
        }
        notes = []
        value = {"url" : "go_gadget_go.com"}
        notifier = NotifierFactory(mission).notifier()

        verification = notifier.verify(current=value, notes=notes)
        self.assertEqual(verification.should_notify, True)


    def test_notifier_notifies_when_notes_contain_different_value(self):
        mission = {
            "mission": {
                "notify": {
                    "distinct_field": {
                        "field" : "url"
                    }
                }
            }
        }
        notes = ["go_gadget_different_go.com"]
        value = {"url" : "go_gadget_go.com"}
        notifier = NotifierFactory(mission).notifier()

        verification = notifier.verify(current=value, notes=notes)
        self.assertEqual(verification.should_notify, True)

    def test_notifier_doesnt_notify_when_notes_contain_thesame(self):
        mission = {
            "mission": {
                "notify": {
                    "distinct_field": {
                        "field" : "url"
                    }
                }
            }
        }
        notes = {"url" : ["go_gadget_go.com"]}
        value = {"url" : "go_gadget_go.com"}
        notifier = NotifierFactory(mission).notifier()

        verification = notifier.verify(current=value, notes=notes)
        self.assertEqual(verification.should_notify, False)


if __name__ == '__main__':
    main()