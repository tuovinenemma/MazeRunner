import os
import pygame
from renderer import Renderer
from level import Level
from events import HandleEvents
from game_over import GameOver
from start_game import Start
from sprites.player import Player
dirname = os.path.dirname(__file__)


class Game:

    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._state = "start"
        self._width = 700
        self._height = 875
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._maze = Level(self._screen)
        self._key = "0"
        self._speed = 1
        self._events = HandleEvents()
        self._start = Start(self._events, self._clock)
        self._end = GameOver(self._clock, self._events)
        self._player = Player(self._speed)
        self._renderer = Renderer(self._player, self._maze, self._screen)
        self._points = 0

    def _start_game(self):

        self._maze._create_maze()
        self._screen.blit(self._player._player,
                          (self._player.rect.x, self._player.rect.y))
        pygame.display.update()

    def _game_running(self):
        while True:
            if self._state == "start":
                self._start._start_screen()
                self._state = "game"
            if self._state == "game":
                self._playing()
                self._state = "game over"
            if self._state == "game over":
                self._end._end_screen()
                self._state = "start"

    def _playing(self):
        self._start_game()
        while True:
            key_pressed = self._events._handle_events()
            if key_pressed == "quit":
                return
            if self._points >= 400 and self._player.rect.x >= 700:
                return
            self._collect_points()
            self._render(key_pressed)
            self._clock.tick(60)

    def _render(self, key_pressed):
        self._player._move_player(key_pressed)
        if self._collision_check():
            self._player._move_player(key_pressed, opposite=True)
        self._renderer.render(self._points)

    def _collision_check(self):
        collision = False
        collision = pygame.sprite.spritecollide(self._player, self._maze._all_walls, False)
        if collision:
            return True
        return False

    def _collect_points(self):
        collision = False
        collision = pygame.sprite.spritecollide(self._player, self._maze._treasures, False)
        for treasure in collision:
            self._maze._treasures.remove(treasure)
            self._maze._all_units.remove(treasure)
            self._points += 100
