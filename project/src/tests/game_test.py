import unittest
from project.src.services.game import Game
from project.src.ui.level import Treasure, Level
from sprites.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player = Player(1)

    def test_is_game_state_correct_in_beginning(self):
        self.assertEqual(str(self.game._state), "start")

    def test_one_point_can_be_collected(self):
        treasure = Treasure(340, 460)
        self.game._maze._treasures.add(treasure)
        self.game._maze._all_units.add(treasure)
        self.game._collect_points()
        self.assertEqual(str(self.game._points), "100")

    def test_more_than_one_point_can_be_collected(self):
        treasure = Treasure(340, 460)
        self.game._maze._treasures.add(treasure)
        self.game._maze._all_units.add(treasure)
        treasure = Treasure(320, 450)
        self.game._maze._treasures.add(treasure)
        self.game._maze._all_units.add(treasure)
        self.game._collect_points()
        self.assertEqual(str(self.game._points), "200")

    def test_player_starts_middle_at_file_maze(self):
        self.assertEqual(str(self.player.rect.x), "340")
        self.assertEqual(str(self.player.rect.y), "460")

    def test_creating_maze_works(self):
        self.game._maze._create_maze()
        self.assertGreater(str(len(self.game._maze._all_units)), "0")
        self.assertGreater(str(len(self.game._maze._all_walls)), "0")
