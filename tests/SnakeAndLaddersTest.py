import unittest

from src.Dice import Dice
from src.SnakeAndLaddersMain import SnakesAndLadders


class SnakesAndLaddersTest(unittest.TestCase):

    def setUp(self):
        self.snake = SnakesAndLadders()

    def test_len_position_table(self):
        self.assertEqual(len(self.snake.snakeAndLadderBoard.positionTable),100)

    def test_fallback_position_table(self):
        self.assertEqual(self.snake.snakeAndLadderBoard.positionTable[14]['fallback'],7)

    def test_random_number_range(self):
        self.snake.dice = Dice()
        num = self.snake.dice.generateDieRoll()
        self.assertTrue(1 <= num <= 6)

    def test_even_random_number(self):
        self.snake.dice = Dice(2)
        num = self.snake.dice.generateDieRoll()
        self.assertTrue(num % 2 == 0)

    def test_even_random_number_range(self):
        self.snake.dice = Dice(2)
        num = self.snake.dice.generateDieRoll()
        self.assertTrue(2 <= num <= 6)

    def test_player_movement(self):
        # assuming testing only first move of the player
        initial = self.snake.player.playerPosition
        self.snake.dice = Dice(2)
        self.snake.player.movePlayer(self.snake.dice.generateDieRoll())
        self.assertNotEqual(initial, self.snake.player.playerPosition)
        self.assertTrue(initial < self.snake.player.playerPosition)

    def test_player_in_bounds(self):
        self.snake.player.playerPosition = 10
        self.assertTrue(self.snake.player.checkIfInBounds())
        self.snake.player.playerPosition = 0

    def test_game_over_by_bounds(self):
        self.snake.player.playerPosition = 101
        self.assertTrue(self.snake.gameOver())
        self.snake.player.playerPosition = 0

    def test_game_over_by_turns(self):
        self.snake.turns = 11
        self.assertTrue(self.snake.gameOver())
        self.snake.turns = 0

    def test_when_square_contains_snake(self):
        self.assertTrue(self.snake.snakeAndLadderBoard.checkSquareContainsSnake(14))

    def test_handle_snake_case(self):
        self.assertEqual(self.snake.snakeAndLadderBoard.getFallbackPostion(14), 7)

