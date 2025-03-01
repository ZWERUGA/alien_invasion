import sys

import pygame

from settings import Settings


class AlienInvasion:
    """
    Основной класс игры 'Alien Invasion'.
    """
    def __init__(self):
        """
        Инициализирует основные настройки игры.
        """
        pygame.init()

        # Настройки игры.
        self.settings = Settings()

        # Задаем размеры и название экрана.
        pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption("Alien Invasion")

    def _run_game(self):
        """
        Запускает основной цикл игры.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai._run_game()
