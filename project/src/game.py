import os
import pygame
from level import *
from events import *
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

    def _start_game(self):

        self._maze._create_maze()
        self._screen.blit(self._player._playerone, (self._player.rect.x, self._player.rect.y))
        self._game_text2()
        
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
            self._events._handle_events()
            if self._events._key_pressed == "quit":
                return
            self._render()
            pygame.display.update()
            self._clock.tick(60)
    
    def _render(self):
        self._screen.fill((255, 255, 255))
        pygame.mouse.set_visible(0)  
        self._maze._make_maze()
        self._move_player()
        self._screen.blit(self._player._playerone, (self._player.rect.x, self._player.rect.y))
        self._game_text2()


    def _game_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        screen.blit(text, pos)
        
    def _game_text2(self):

        self._game_text(f'PRESS "Q" TO QUIT THE GAME', self._screen, [250, 845], 25, (0, 0, 0), 'arial black')



    def _move_player(self):
        key_pressed = self._events._key_pressed
        self._key = key_pressed

        if key_pressed == "l":
            self._player.rect.x -= 1
        if key_pressed == "r":
            self._player.rect.x += 1
        if key_pressed == "u":
            self._player.rect.y -= 1
        if key_pressed == "d":
            self._player.rect.y += 1
        
        if self._player.rect.x < 0:
            self._player.rect.x = 700
            self._screen.blit(self._player._playerone, (self._player.rect.x, self._player.rect.y))
            
        elif self._player.rect.x > 700:
            self._player.rect.x = 0
            self._screen.blit(self._player._playerone, (self._player.rect.x, self._player.rect.y))