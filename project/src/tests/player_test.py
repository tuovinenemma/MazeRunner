import unittest
from sprites.player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player = Player(1)
    
    def test_player_can_move_right(self):
        self.player._move_player(direction="r")
        self.assertEqual(str(self.player.rect.x), "324")
    
    def test_player_can_move_left(self):
        self.player._move_player(direction="l")
        self.assertEqual(str(self.player.rect.x), "322")

    def test_player_can_move_up(self):
        self.player._move_player(direction="u")
        self.assertEqual(str(self.player.rect.y), "624")

    def test_player_can_move_down(self):
        self.player._move_player(direction="d")
        self.assertEqual(str(self.player.rect.y), "626")