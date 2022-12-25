import unittest
from ui.game_over import GameOver
from mock import Mock

class TestGameOver(unittest.TestCase):
    def setUp(self):
        self.game_over = GameOver(clock=None, events=None)

    def test_end_text2_sets_white_screen_color(self):
        self.game_over._end_text2()
        self.assertEqual(self.game_over._screen.get_at((0, 0)), (255, 255, 255))
        
    def test_end_text1_renders_text_at_correct_position(self):
        self.game_over._end_text1('test', self.game_over._screen, [100, 100], 30, (0, 0, 0), 'arial black')
        self.assertEqual(self.game_over._screen.get_at((100, 100)), (0, 0, 0))
        
    def test_end_text1_centers_text_when_middle_flag_is_set(self):
        self.game_over._end_text1('test', self.game_over._screen, [100, 100], 30, (0, 0, 0), 'arial black', middle=True)
        self.assertEqual(self.game_over._screen.get_at((75, 100)), (0, 0, 0))
        
    def test_render_calls_end_text2(self):
        self.game_over._end_text2 = Mock()
        self.game_over._render()
        self.assertTrue(self.game_over._end_text2.called)

    def test_end_game_sets_screen_color(self):
        self.game_over._end_game()
        self.assertEqual(self.game_over._screen.get_at((0, 0)), (255, 255, 255))