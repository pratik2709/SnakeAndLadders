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

    def test_player_in_bounds(self):
        self.snake.playerPosition = 10
        self.assertTrue(self.snake.checkIfInBounds())
        self.snake.playerPosition = 0

    def test_game_over_by_bounds(self):
        self.snake.playerPosition = 101
        self.assertTrue(self.snake.gameOver())
        self.snake.playerPosition = 0

    def test_game_over_by_turns(self):
        self.snake.turns = 11
        self.assertTrue(self.snake.gameOver())
        self.snake.turns = 0

    def test_when_square_contains_snake(self):
        self.snake.playerPosition = 14
        self.assertTrue(self.snake.checkSquareContainsSnake())

    def test_handle_snake_case(self):
        self.snake.playerPosition = 14
        self.snake.handleCaseWhenSquareContainsSnake()
        self.assertEqual(self.snake.playerPosition, 7)

