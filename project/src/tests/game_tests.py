import unittest
from game import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        
    def test_does_game_state_work(self):
