import pygame
import random


def main():
    pygame.init()
    pygame.display.set_mode((600, 600))
    pygame.display.set_caption('A template for graphical games with two moving dots')
    w_surface = pygame.display.get_surface()
    game = Game(w_surface)
    game.play()
    pygame.quit()


class Game:

    def __init__(self, surface):
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True
        self.x = 5
        self.y = 5
        self.init_image = pygame.image.load('image0.bmp')
        self.tile = Tile(self.surface, self.init_image, self.x, self.y)
        self.frame_counter = 0

    def play(self):
        while not self.close_clicked:
            self.mousx, self.mousy = self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS)

    def handle_events(self):
        mousx, mousy = 0, 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousx, mousy = event.pos
        return mousx, mousy

    def draw(self):
        """self.surface.fill(self.bg_color)"""
        self.x = self.y = 5
        for i in range(16):
            if i % 4 == 0 and i != 0:
                self.y += 110
            self.x = (i % 4) * 110 + 5
            self.tile.update(self.x, self.y)
            tile_num = self.decide_tile(self.mousx, self.mousy)
            if tile_num is not None and tile_num != 0:
                self.tile.show_tile(tile_num)
                self.mousx = self.mousy = 0
            self.tile.draw()
            if tile_num is not None and tile_num != 0:
                self.tile.hide_tile()
        pygame.display.update()

    def update(self):
        self.frame_counter = self.frame_counter + 1

    def decide_continue(self):
        pass

    def decide_tile(self, mousx, mousy):
        if mousx != 0 and mousy != 0:
            tile = 0
            if 5 <= mousy <= 105:
                if 5 <= mousx <= 435:
                    tile = int((mousx - 5) / 110) + 1
            elif 115 <= mousy <= 215:
                if 5 <= mousx <= 435:
                    tile = int((mousx - 5) / 110) + 5
            elif 225 <= mousy <= 325:
                if 5 <= mousx <= 435:
                    tile = int((mousx - 5) / 110) + 9
            elif 335 <= mousy <= 435:
                if 5 <= mousx <= 435:
                    tile = int((mousx - 5) / 110) + 13
            return tile


class Tile:

    def __init__(self, surface, image, x, y):
        self.surface = surface
        self.hidden = pygame.image.load('image0.bmp')
        self.image = self.hidden
        self.x = x
        self.y = y
        self.cards = ['image1.bmp', 'image2.bmp', 'image3.bmp', 'image4.bmp', 'image5.bmp', 'image6.bmp', 'image7.bmp',
                      'image8.bmp', 'image1.bmp', 'image2.bmp', 'image3.bmp', 'image4.bmp', 'image5.bmp', 'image6.bmp',
                      'image7.bmp', 'image8.bmp']
        random.shuffle(self.cards)

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

    def update(self, x, y):
        self.x = x
        self.y = y

    def show_tile(self, tile):
        index = tile - 1
        self.image = pygame.image.load(self.cards[index])
    def hide_tile(self):
        self.image = self.hidden


main()
