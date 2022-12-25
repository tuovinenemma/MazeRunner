import os
import pygame
from ui.renderer import Renderer
from ui.level import Level
from services.events import HandleEvents
from ui.game_over import GameOver
from ui.start_game import Start
from sprites.player import Player
from sprites.monster import Monster
from ui.levels import MAZE_ONE, MAZE_TWO

dirname = os.path.dirname(__file__)


class Game:
    """Luokka, joka vastaa pelin kulusta
    """

    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._state = "start"
        self._width = 700
        self._height = 875
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._maze = Level(self._screen)
        self._key = "0"
        self._points = 0
        self._speed = 1
        self._player_speed = 1
        self._events = HandleEvents()
        self._start = Start(self._events, self._clock)
        self._end = GameOver(self._clock, self._events)
        self._player = Player(self._player_speed)
        self._renderer = Renderer(self._player, self._maze, self._screen)
        self._monsters = []
        self._all_monsters = pygame.sprite.Group()
        self._lives = 5

    def _start_game(self):
        if self._state == "game":
            self._maze._empty_maze()
            self._all_monsters.empty()
            self._monsters = []
            self._maze._create_maze(MAZE_ONE)
        if self._state == "game2":
            self._maze._empty_maze()
            self._all_monsters.empty()
            self._monsters = []
            self._maze._create_maze(MAZE_TWO)
            self._player._center_player()
            self._points = self._points
        self._screen.blit(self._player._player,
                          (self._player.rect.x, self._player.rect.y))
        self._make_monsters()
        self._all_monsters.add(self._monsters)
        for monster in self._monsters:
            self._screen.blit(monster._monster, (monster.rect.x, monster.rect.y))
        pygame.display.update()

    def _game_running(self):
        """Tarkistaa pelin tilanteen
        """
        while True:
            if self._state == "start":
                self._start._start_screen()
                self._state = "game"
            if self._state == "game":
                self._playing()
                self._state = "game over"
            if self._state == "game2":
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
                self._points = 0
                return
            if self._lives == 0:
                self._points = 0
                return
            self._collect_points()
            self._check_collision_monster()
            self._exit_level()
            for monster in self._all_monsters:
                monster._monster_can_move(self._maze._all_walls)
            self._render(key_pressed)
            self._clock.tick(60)

    def _render(self, key_pressed):
        self._player._move_player(key_pressed)
        if self._collision_check():
            self._player._move_player(key_pressed, opposite=True)
        self._renderer.render(self._points, self._lives)
        self._all_monsters.draw(self._screen)
        pygame.display.update()

    def _collision_check(self):
        """Tarkistaa törmäyksen
        """
        collision = False
        collision = pygame.sprite.spritecollide(self._player, self._maze._all_walls, False)
        if collision:
            return True
        return False

    def _check_collision_monster(self):
        collision = False
        collision = pygame.sprite.spritecollide(self._player, self._all_monsters, False)
        for monster in collision:
            self._all_monsters.remove(monster)
            self._lives -= 1

    def _collect_points(self):
        """Kerää pisteitä
        """
        collision = False
        collision = pygame.sprite.spritecollide(self._player, self._maze._treasures, False)
        collision_potions = pygame.sprite.spritecollide(self._player, self._maze._potion, False)
        for treasure in collision:
            self._maze._treasures.remove(treasure)
            self._maze._all_units.remove(treasure)
            self._points += 100
        for potion in collision_potions:
            self._maze._potion.remove(potion)
            self._maze._all_units.remove(potion)
            self._player_speed += 1


    def _exit_level(self):
        """Siirtää pelaajan seuraavaan kenttään
        """
        collision = False
        collision = pygame.sprite.spritecollide(self._player, self._maze._exit, False)
        for exit in collision:
            if self._state == "game":
                self._maze._exit.remove(exit)
                self._maze._all_units.remove(exit)
                self._state = "game2"
                self._start_game()

            elif self._state == "game2":
                self._maze._exit.remove(exit)
                self._maze._all_units.remove(exit)
                self._state = "game over"
                self._points = 0
                self._game_running()


    def _make_monsters(self):
        monster_count = self._start._monsters_count
        for x in range(monster_count):
            monster = Monster()
            self._monsters.append(monster)
            self._all_monsters.add(monster)
