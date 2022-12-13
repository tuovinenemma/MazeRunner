import sys
import pygame

class GameEvents:

    def get(self):
        return pygame.event.get()


class HandleEvents:
    """Luokka, joka huolehtii mistä näppäimestä ollaan painettu
    """

    def __init__(self):
        self._events = GameEvents()
        self._quit = False
        self._key_pressed = "0"

    def _handle_events(self):

        for event in self._events.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._key_pressed = "l"
                if event.key == pygame.K_RIGHT:
                    self._key_pressed = "r"
                if event.key == pygame.K_UP:
                    self._key_pressed = "u"
                if event.key == pygame.K_DOWN:
                    self._key_pressed = "d"
                if event.key == pygame.K_SPACE:
                    self._key_pressed = "space"
                if event.key == pygame.K_q:
                    self._key_pressed = "quit"
                if event.key == pygame.K_r:
                    self._key_pressed = "restart"
                if event.key == pygame.K_e:
                    self._key_pressed = "exit"

            if event.type == pygame.QUIT:
                sys.exit()

        return self._key_pressed
