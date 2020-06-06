import unittest

from SnakeAndLadders import SnakesAndLadders


class SnakesAndLaddersTest(unittest.TestCase):

    def setUp(self):
        self.snake = SnakesAndLadders()

    def test_len_position_table(self):
        self.assertEqual(len(self.snake.positionTable),100)

    def test_fallback_position_table(self):
        self.assertEqual(self.snake.positionTable[14]['fallback'],7)

    def test_random_number_range(self):
        num = self.snake.generateRandomNumber()
        self.assertTrue(1 <= num <= 6)
