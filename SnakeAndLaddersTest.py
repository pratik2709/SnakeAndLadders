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

    def test_even_random_number(self):
        num = self.snake.generateEvenRandomNumber()
        self.assertTrue(num % 2 == 0)

    def test_even_random_number_range(self):
        num = self.snake.generateEvenRandomNumber()
        self.assertTrue(2 <= num <= 6)

    def test_player_movement(self):
        # assuming testing only first move of the player
        initial = self.snake.playerPosition
        self.snake.movePlayer()
        self.assertNotEqual(initial, self.snake.playerPosition)
        self.assertTrue(initial < self.snake.playerPosition)