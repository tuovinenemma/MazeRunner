import unittest
from services.game import Game
from ui.level import Treasure, Exit
from ui.levels import MAZE_ONE
from sprites.player import Player
from Main import main

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

    def test_player_starts_middle_at_maze(self):
        self.assertEqual(str(self.player.rect.x), "330")
        self.assertEqual(str(self.player.rect.y), "465")

    def test_creating_maze_works(self):
        self.game._maze._create_maze(MAZE_ONE)
        self.assertGreater(str(len(self.game._maze._all_units)), "0")
        self.assertGreater(str(len(self.game._maze._all_walls)), "0")

    def test_exit_starts_a_new_level(self):
        exit = Exit(0, 0)
        self.game._maze._exit.add(exit)
        self.game._maze._all_units.add(exit)
        
        self.player.rect.x = 0
        self.player.rect.y = 0
        
        self.game._exit_level()
        self.assertEqual(self.game._state, "start")


    def test_game_screen_has_correct_dimensions(self):
        self.assertEqual(self.game._width, 700)
        self.assertEqual(self.game._height, 875)

    def test_player_speed_is_set_correctly(self):
        self.assertEqual(self.game._player._speed, 1)

    def test_game_clock_has_correct_fps(self):
        self.assertEqual(self.game._clock.get_fps(), 0.0)


    def test_game_position_is_updated_correctly(self):
        initial_position = self.player.rect.x, self.player.rect.y

        self.player._move_player(direction="r")

        current_position = self.player.rect.x, self.player.rect.y

        self.assertNotEqual(initial_position, current_position)


    def test_render(self):
        self.game._state = "game"
        
        player_x = self.player.rect.x
        player_y = self.player.rect.y
        self.game._render(None)
        self.assertEqual(self.player.rect.x, player_x)
        self.assertEqual(self.player.rect.y, player_y)
        
        self.player._move_player(direction="r")
        self.assertEqual(self.player.rect.x, player_x + self.player._speed)
        self.assertEqual(self.game._player.rect.y, player_y)

    def test_playing_calls_start_game(self):
        self.game._playing = lambda: self.game._start_game()
        self.game._playing()
        self.assertEqual(self.game._state, "start")

    def test_playing_exits_on_quit_event(self):
        self.game._events._key_pressed = "quit"
        self.game._playing()
        self.assertEqual(self.game._points, 0)

    def test_player_is_moved_left(self):
        initial_position = self.player.rect.x, self.player.rect.y

        self.player._move_player(direction="l")

        current_position = self.player.rect.x, self.player.rect.y

        self.assertEqual(initial_position[0] - self.player._speed, current_position[0])
        self.assertEqual(initial_position[1], current_position[1])


    def test_collision_check(self):
        self.player.rect.x = 100
        self.player.rect.y = 100
        self.game._maze._create_maze(MAZE_ONE)
        walls = self.game._maze._all_walls

        self.assertFalse(self.game._collision_check())

        self.player.rect.x = 200
        self.player.rect.y = 200

        self.assertFalse(self.game._collision_check())

