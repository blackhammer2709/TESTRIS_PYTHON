from settings import *
import sys
import pygame.freetype as ft


class Screen:
    def __init__(self, app):
        # self.app
        pass

    def update(self):
        pass

    def draw(self):
        pass


class StartScreen:
    def __init__(self, app):
        # self.app
        self.screen = app.screen
        self.font = ft.Font(FONT_PATH)

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.font.render_to(self.screen, (WIN_W * 0.3, WIN_H * 0.45),
                            text="TETRIS CLONE", fgcolor=(255, 20, 147), size=TILE_SIZE)

    # agregar self.inicio, self.puntos, self.config
    # funciones para botones


class PauseScreen:
    def __init__(self, app):
        self.screen = app.screen
# TODO estiliziar

    def draw(self):
        pause_text = pg.font.SysFont('Arial', 32).render(
            'Pause', True, pg.color.Color('White'))
        self.screen.blit(
            pause_text, (FIELD_RES[0] // 2 - 40, FIELD_RES[1] // 2))
        pass
