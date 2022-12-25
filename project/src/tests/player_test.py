import unittest
from sprites.player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player = Player(1)

    def test_player_can_move_right(self):
        self.player._move_player(direction="r")
        self.assertEqual(str(self.player.rect.x), "331")

    def test_player_can_move_left(self):
        self.player._move_player(direction="l")
        self.assertEqual(str(self.player.rect.x), "329")

    def test_player_can_move_up(self):
        self.player._move_player(direction="u")
        self.assertEqual(str(self.player.rect.y), "464")

    def test_player_can_move_down(self):
        self.player._move_player(direction="d")
        self.assertEqual(str(self.player.rect.y), "466")

    def test_player_stops_at_wall_when_going_down(self):
        for i in range(100):
            self.player._move_player(direction="d")
        self.assertLess(str(self.player.rect.y), "800")

    def test_player_stops_at_wall_going_up(self):
        for i in range(100):
            self.player._move_player(direction="u")
        self.assertLess(str(self.player.rect.y), "700")