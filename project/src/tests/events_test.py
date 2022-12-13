import unittest
from services.events import HandleEvents
import pygame

class TestHandleEvents(unittest.TestCase):
    def setUp(self):
        self.events = HandleEvents()

    def test_handle_events(self):
        self.events._events.get = lambda: [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)]
        self.assertEqual(self.events._handle_events(), "space")

        self.events._events.get = lambda: [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)]
        self.assertEqual(self.events._handle_events(), "l")

        self.events._events.get = lambda: [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)]
        self.assertEqual(self.events._handle_events(), "r")

        self.events._events.get = lambda: [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)]
        self.assertEqual(self.events._handle_events(), "u")

        self.events._events.get = lambda: [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)]
        self.assertEqual(self.events._handle_events(), "d")


