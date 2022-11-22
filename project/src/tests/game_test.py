import unittest
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_is_game_state_correct_in_beginning(self):
        self.assertEqual(str(self.game._state), "start")

