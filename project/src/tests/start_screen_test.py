import unittest
import pygame
from ui.start_game import Start
from services.events import HandleEvents

class TestStart(unittest.TestCase):
    def setUp(self):
        self.events = HandleEvents()
        self.clock = pygame.time.Clock()
        self.start = Start(self.events, self.clock)

    def test_start_screen_updates_state_to_start(self):
        self.start._start_screen()
        self.assertEqual(self.start._state, "start")

    def test_start_screen_sets_monsters_count_to_10(self):
        self.events._key_pressed = "b"
        self.start._start_screen()
        self.assertEqual(self.start._monsters_count, 10)

    def test_start_text1_centers_text(self):
        self.start._screen.fill((255, 255, 255))
        self.start._start_text1('TEST', self.start._screen, [self.start._width//2, self.start._height//2], 45, (0, 0, 0), 'arial black', middle=True)
        text_rect = self.start._screen.get_rect()
        self.assertEqual(text_rect.centerx, self.start._width//2)
        self.assertEqual(text_rect.centery, self.start._height//2)

    def test_start_text3_displays_text(self):
        self.start._screen.fill((255, 255, 255))
        self.start._start_text3()
        text = self.start._screen.get_at((self.start._width//2, self.start._height//2-40))
        self.assertEqual(text, (255, 255, 255))

    def test_start_text1_displays_text(self):
        self.start._screen.fill((255, 255, 255))
        self.start._start_text1("TEST TEXT", self.start._screen, [100, 100], 30, (0, 0, 0), "arial black")
        text = self.start._screen.get_at((100, 100))
        self.assertEqual(text, (255, 255, 255))

