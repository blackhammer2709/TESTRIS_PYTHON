import pygame as pg

vec = pg.math.Vector2

FPS = 60
MOVE_TICKER = int(FPS/10)
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (34, 4, 204)

SPRITE_DIR_PATH = 'assets/sprites'
FONT_PATH = 'assets/fonts/FREAKSOFNATUREMASSIVE.ttf'

ANIM_TIME_INTERVAL = 250

FAST_ANIM_TIME_INTERVAL = 30

TILE_SIZE = 30
FIELD_SIZE = FIELD_W, FIELD_H = 13, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0

WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * \
    FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_W // 2, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

TETRAMINOS = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (0, 1), (0, -1), (-1, -1)],
    'L': [(0, 0), (0, 1), (0, -1), (1, -1)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)],
    '0': [(0, 0), (0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1), (2, 0)],
    'H': [(0, 0), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1)],
    'C': [(0, 0), (0, -1), (1, -1), (0, 1), (1, 1)],
    '.': [(0, 0)]
}