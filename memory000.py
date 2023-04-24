import time
import pygame
import random


def main():
    pygame.init()
    pygame.display.set_mode((600, 500))
    pygame.display.set_caption('Memory')
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
        self.tile = Tile(self.surface, self.x, self.y)
        self.frame_counter = 0
        self.cards = ['image1.bmp', 'image2.bmp', 'image3.bmp', 'image4.bmp', 'image5.bmp', 'image6.bmp', 'image7.bmp',
                      'image8.bmp', 'image1.bmp', 'image2.bmp', 'image3.bmp', 'image4.bmp', 'image5.bmp', 'image6.bmp',
                      'image7.bmp', 'image8.bmp']
        random.shuffle(self.cards)
        # create three lists: all shown, all hidden, current shown
        self.tile_lst, self.hid_lst, self.game_lst = self.creat_lst()
        self.compare = []
        self.paired = []
        self.score = 0

    def play(self):
        while not self.close_clicked:
            # get the coordinates of mouse button down and handle the events
            self.mousx, self.mousy = self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS)

    def draw(self):
        # initialize the self.x and self.y every time when calling draw function
        self.x = self.y = 5
        # if the tow tiles are different
        if len(self.compare) == 2 and self.compare[0] != self.compare[1]:
            #show the two cards for 0.5 seconds
            time.sleep(0.5)
            # then hide the two cards
            for i in self.game_lst:
                for j in i:
                    if j in self.compare:
                        self.game_lst[self.game_lst.index(i)][i.index(j)] = 'image0.bmp'
            # if two cards are different, score + 1
            self.score += 1
            # after hide the two cards, initialize the self.compare list to get ready for the next click
            self.compare = []
        # this function returns which tile was clicked
        tile_num = self.decide_tile(self.mousx, self.mousy)
        # if nothing clicked, the function will return None
        # if return 0 means didn't click the tile
        if tile_num is not None and tile_num != 0:
            # return two indexes
            # indicates the tile in the game_lst
            a, b = self.tile_index(tile_num)
            # nothing will process if click shown tiles again
            if self.game_lst[a][b] not in self.paired:
                # if there is no element in self.compare,
                # this shows this is the first tile clicked
                if len(self.compare) == 0:
                    # use old_tile to store which tile is firstly clicked
                    self.old_tile = tile_num
                    a, b = self.tile_index(tile_num)
                    # append the name of picture of the firstly clicked tile to the compare list
                    self.compare.append(self.tile_lst[a][b])
                    # change the game list to show the clicked tile
                    self.game_lst[a][b] = self.compare[0]
                # if lenth is 1, this is the second click
                elif len(self.compare) == 1:
                    # if the do not click the same tile as the first one
                    # we can continue
                    if self.old_tile != tile_num:
                        a, b = self.tile_index(tile_num)
                        # also add this tile name to the compare list
                        self.compare.append(self.tile_lst[a][b])
                        self.game_lst[a][b] = self.compare[1]
                # if lenth of compare list is 2
                if len(self.compare) == 2:
                    if self.compare[0] == self.compare[1]:
                        self.paired.append(self.compare[0])
                        self.compare = []
                    elif self.compare[0] != self.compare[1]:
                        self.draw_tiles()
        elif tile_num is None and len(self.compare) != 2:
            self.draw_tiles()
            self.mousx = self.mousy = 0
        self.draw_score()
        pygame.display.update()

    def handle_events(self):
        # initialize the mouse coordinates
        mousx, mousy = 0, 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousx, mousy = event.pos
        return mousx, mousy

    def update(self):
        # frame_counter will add 1 in speed 60 FPS
        self.frame_counter += 1
        # if frame_counter % 60 == 0 means 60 frames pass so 1 second pass
        if self.frame_counter % 60 == 0:
            self.score += 1

    def decide_continue(self):
        # if all tiles are paired
        if self.game_lst == self.tile_lst:
            self.continue_game = False

    def decide_tile(self, mousx, mousy):
        # not 0 means button down
        if mousx != 0 and mousy != 0:
            # initialize the tile
            tile = 0
            # the first row
            if 5 <= mousy <= 105:
                # the left edge of the first tile
                # and the right edge of the fourth tile
                if 5 <= mousx <= 435:
                    # int() is to throw the decimal part, so + 1
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

    def creat_lst(self):
        lst = []
        hid_lst = []
        game_lst = []
        i = 0
        # 16 elements in total, so loop 16 times
        while i < 16:
            # 4 lists inside the list so repeat 4 times
            for j in range(4):
                in_lst = []
                in_lst1 = []
                # 4 elements in each list so repeat 4 times
                for k in range(4):
                    in_lst.append(self.cards[i])
                    in_lst1.append('image0.bmp')
                    i += 1
                lst.append(in_lst)
                hid_lst.append(in_lst1)
                game_lst.append(in_lst1)
        return lst, hid_lst, game_lst

    def draw_tiles(self):
        i = 0
        # 16 tiles so loop 16 times
        while i < 16:
            # for the 4 lists in the list
            for j in self.game_lst:
                # for every tiles inside the list
                for k in j:
                    # i start from 0 so i != to include the first row
                    # if i % 4 == 0 means i is added to 4,
                    # the shows the firs row has been printed
                    if i % 4 == 0 and i != 0:
                        # then start the second row
                        # a picture is 100 add 10 interval
                        self.y += 110
                    # 5 from the edge of the screen
                    # add 110 after each picture printed
                    self.x = (i % 4) * 110 + 5
                    # load first
                    self.tile.draw(pygame.image.load(k), self.x, self.y)
                    i += 1
    # this function input the number which tile is clicked
    # returns the two indexes to get the name of corresponding picture from the nested list
    def tile_index(self, tile):
        i = 0
        j = 0
        # first row
        if 1 <= tile <= 4:
            i = 0
            # index start from 0
            j = ((tile - 1) % 4)
        # second row
        elif 5 <= tile <= 8:
            i = 1
            j = ((tile - 1) % 4)
        # third row
        elif 9 <= tile <= 12:
            i = 2
            j = ((tile - 1) % 4)
        # fourth row
        elif 13 <= tile <= 16:
            i = 3
            j = ((tile - 1) % 4)
        return int(i), int(j)

    def draw_score(self):
        score_string = str(self.score)
        score_font = pygame.font.SysFont('', 72)
        score_image = score_font.render(score_string, True,
                                        pygame.Color('white'), self.bg_color)
        score_top_right_corner = (540, 0)
        self.surface.blit(score_image, score_top_right_corner)


class Tile:

    def __init__(self, surface, x, y):
        self.surface = surface
        self.hidden = pygame.image.load('image0.bmp')
        self.image = self.hidden
        self.x = x
        self.y = y

    def draw(self, image, x, y):
        self.surface.blit(image, (x, y))


main()
