from application.criteria import CriteriaFactory, CriteriaSimilar
from unittest import TestCase, main

class CriteriaSimilarTest(TestCase):

    def setUp(self):
        self.config = {
            "mission": {
                "compare": {
                    "similar" : "Text"
                }
            }
        }

    def test_criteria_has_valid_type(self):
        criteria = CriteriaFactory(self.config).criteria()
        self.assertIsInstance(criteria, CriteriaSimilar)


    def test_criteria_matches_similar(self):
        criteria = CriteriaFactory(self.config).criteria()
        match = criteria.test("This text")
        self.assertTrue(match.found, True)

if __name__ == '__main__':
    main()