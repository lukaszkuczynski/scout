from unittest import main, TestCase
from application.similarity_calculator import SimilarityCalculator

class SimilarityTest(TestCase):

    def setUp(self):
        self.calculator = SimilarityCalculator(threshold=0.1)

    def test_similar_1(self):
        text1 = "Go to China"
        text2 = "China market is alive"
        self.assertTrue(self.calculator.are_similar(text1, text2))

    def test_notsimilar_1(self):
        text1 = "Go to Bulgaria sweet man, fishing time"
        text2 = "Sweets are not good for me, I am fat"
        self.assertFalse(self.calculator.are_similar(text1, text2))


if __name__ == '__main__':
    main()