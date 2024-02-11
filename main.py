from settings import *
from screen import PauseScreen, StartScreen
from tetris import Tetris, Text
import sys
import pathlib
import os
# hacer mas rapido tras x cantidad de puntos
# modificar colores gradualmente con ticks
# rotar pantalla y reorganizar tras x cantidad de puntos
# algun modificador?
# def get_path(self, filename):
#   if hasattr(sys, "_MEIPASS"):
#      return os.path.join(sys._MEIPASS, filename)
# else:
#    return filename
# juegos deben ser mas factorizados, principio hacer una sola cosa y que la haga bien


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return pathlib.Path(sys._MEIPASS)/filename
    else:
        return filename


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris")
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)
        self.startscreen = StartScreen(self)
        self.psscreen = PauseScreen(self)

        self.pause = False
        self.start = False
        self.current_lines = 0
        self.current_level = 0
        self.move_ticker = 0

    def load_images(self):
        files = [get_path(item) for item in pathlib.Path(
            SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(
            image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        if self.pause:
            return
        # aqui deberia ir un if igual que el de arriba pero con self.start
        else:
            self.tetris.update()
            self.clock.tick(FPS)
            if self.move_ticker > 0:
                self.move_ticker -= 1

    def draw(self):
        if self.pause:
            self.psscreen.draw()
        if self.start:
            self.startscreen.draw()
        else:
            self.screen.fill(color=BG_COLOR)
            self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
            self.tetris.draw()
            self.text.draw()
        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if not self.pause:
                if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                    self.tetris.control(pg.K_UP)
                elif event.type == self.user_event:
                    self.anim_trigger = True
                elif event.type == self.fast_user_event:
                    self.fast_anim_trigger = True

            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.start = not self.start
                # self.pause = not self.pause
        if not self.pause:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                if self.move_ticker == 0:
                    self.move_ticker = MOVE_TICKER
                    self.tetris.control(pg.K_LEFT)
            elif keys[pg.K_RIGHT]:
                if self.move_ticker == 0:
                    self.move_ticker = MOVE_TICKER
                    self.tetris.control(pg.K_RIGHT)
            elif keys[pg.K_DOWN]:
                if self.move_ticker == 0:
                    self.move_ticker = MOVE_TICKER
                    self.tetris.control(pg.K_DOWN)

            elif not keys[pg.K_DOWN]:
                self.tetris.control(None)

    def run(self):
        while True:
            #o aqui deberia modificar para ver el start
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
